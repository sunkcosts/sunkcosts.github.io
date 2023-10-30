from __future__ import annotations

import sys
import json
import requests
import pandas as pd
import numpy as np
from numpy.typing import ArrayLike
from pathlib import Path
from pydantic.dataclasses import dataclass
from pydantic import BaseModel, field_validator
from scipy import integrate, optimize
from scipy.stats import skewnorm
from loguru import logger as l

# from netCDF4._netCDF4 import Dataset as NCD

VALID_CONFIDENCE_LEVELS = {"medium", "high"}
VALID_SCENARIOS = {"126", "245", "585"}

# TODO: add regional parsing
# TODO: integrate old genetic SND fiting model for better curve fits


SCENARIO_FILES = {
    "low": {
        "126": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/low.126.ssp",
        "245": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/low.245.ssp",
        "585": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/low.585.ssp",
    },
    "medium": {
        "126": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/med.126.ssp",
        "245": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/med.245.ssp",
        "585": "https://github.com/sunkcosts/ar6_slp_global_confidence_data/raw/main/data/ssp/med.585.ssp",
    },
}


class SkewedNormalDistribution:
    def __init__(self) -> None:
        # self.model = lambda x: x
        self.a = None
        self.loc = None
        self.scale = None
        self.__trained = False

    def __check_fit(self) -> None:
        if not self.__trained:
            raise Exception("you must fit the model parameters first")

    def model(self, x: int | float | ArrayLike) -> int | float | ArrayLike:
        return skewnorm.pdf(x, self.a, self.loc, self.scale)

    def fit(self, distribution: ArrayLike) -> None:
        self.a, self.loc, self.scale = skewnorm.fit(distribution)
        self.__trained = True
        l.success(
            f"distribution fit with params: a={self.a}, loc={self.loc}, scale={self.scale}"
        )

    @property
    def vmean(self) -> float | int:
        "mean x value of the distribution"
        self.__check_fit()
        return skewnorm.stats(self.a, self.loc, self.scale, moments="m")  # type: ignore

    @property
    def pmean(self) -> float | int:
        "probability density at mean value of the distribution"
        self.__check_fit()
        return self.model(self.vmean)  # type: ignore

    @property
    def vmed(self) -> float | int:
        "median x value of the distribution"
        self.__check_fit()
        return skewnorm.ppf(0.5, self.a, self.loc, self.scale)  # type: ignore

    @property
    def pmed(self) -> float | int:
        "probability density at median value of the distribution"
        self.__check_fit()
        return self.model(self.vmed)  # type: ignore

    @property
    def vmax(self) -> float | int:
        "x value at maximum probability value of PDF"
        self.__check_fit()
        return optimize.fmin(lambda x: -self.model(x), self.loc, disp=False)[0]  # type: ignore

    @property
    def pmax(self) -> float | int:
        "maximum probability value of PDF"
        self.__check_fit()
        result = optimize.fmin(lambda x: -self.model(x), self.loc, disp=False)  # type: ignore
        return self.model(result[0])  # type: ignore

    @property
    def pmid(self) -> float | int | ArrayLike:
        "midpoint between meanp and maxp"
        self.__check_fit()
        return (self.pmean + self.pmax) / 2

    @property
    def vmid(self) -> float | int:
        "midpoint between meanv and maxv"
        self.__check_fit()
        return (self.vmean + self.vmax) / 2

    @property
    def v_at_pmid(self) -> float | int:
        self.__check_fit()
        return optimize.fsolve(lambda x: self.model(x) - self.pmid, self.vmean)[0]  # type: ignore

    @property
    def p_at_vmid(self) -> float | int | ArrayLike:
        self.__check_fit()
        return self.model(self.vmid)

    def interval(
        self,
        lower: float = -float("inf"),
        upper: float = float("inf"),
    ) -> float:
        "integrated area under PDF curve for given lower and upper bound interval"
        if not self.model is None:
            return round(
                integrate.quad(self.probability, lower, upper)[0],
                4,
            )
        else:
            raise Exception("you must fit the model parameters first")

    def probability(self, x: float | ArrayLike) -> float | ArrayLike:
        "PDF function value at input x"
        if not self.model is None:
            return self.model(x)
        else:
            raise Exception("you must fit the model parameters first")


class ReferenceLinks(BaseModel):
    wiki: str
    doi: str


class DownloadLinks(BaseModel):
    dataset: str
    raw: str
    ssp: str


class Metadata(BaseModel):
    description: str
    reference: ReferenceLinks
    download: DownloadLinks


@dataclass
class Data:
    _json: dict

    def __post_init__(self) -> None:
        self.table = self.__make_dataframe(self._json)

    @staticmethod
    def __make_dataframe(_json: dict) -> pd.DataFrame:
        dataframe = pd.DataFrame(_json["sea_level_change_mm"])
        dataframe.index = _json["years"]
        dataframe.columns = _json["quantiles"]
        return dataframe

    @property
    def quantiles(self):
        return self._json["quantiles"]

    @property
    def years(self):
        return self._json["years"]

    @property
    def slcmm(self) -> ArrayLike:
        "returns sea level change matrix for sea level values in mm"
        return np.array(self._json["sea_level_change_mm"])

    def slcmm_year(self, year: int) -> ArrayLike:
        "returns sea level change array for sea level values in mm for a given year"
        return np.array(self.table.loc[year].values)


@dataclass
class Forecast:
    data: Data

    def __post_init__(self) -> None:
        self.models = dict()

    def train(self) -> None:
        for year in self.data.years:
            snd = SkewedNormalDistribution()
            snd.fit(self.data.slcmm_year(year=year))
            self.models[year] = snd

    def pmax(self, year: int) -> float:
        return self.models[year].pmax

    def vmax(self, year: int) -> float:
        return self.models[year].vmax

    def pmean(self, year: int) -> float:
        return self.models[year].pmean

    def vmean(self, year: int) -> float:
        return self.models[year].vmean

    def pmed(self, year: int) -> float:
        return self.models[year].pmed

    def vmed(self, year: int) -> float:
        return self.models[year].vmed

    def pmid(self, year: int) -> float:
        return self.models[year].pmid

    def vmid(self, year: int) -> float:
        return self.models[year].vmid

    def v_at_pmid(self, year: int) -> float | int:
        return self.models[year].v_at_pmid

    def p_at_vmid(self, year: int) -> float | int:
        return self.models[year].p_at_vmid

    def model(self, year: int):
        return self.models[year]

    def interval(self, lower: int | float, upper: int | float, year: int) -> float:
        return self.models[year].interval(lower=lower, upper=upper)

    def probability(self, x: int | float | ArrayLike, year: int) -> float | ArrayLike:
        return self.models[year].probability(x=x)


@dataclass
class SLP:
    """
    Derived from ar6/global/confidence_output_files.
    """

    confidence: str
    scenario: str
    metadata: Metadata
    data: Data

    @field_validator("confidence")
    def __valid_confidence(cls, confidence: str) -> str:
        if not confidence in VALID_CONFIDENCE_LEVELS:
            raise ValueError(f"confidence must be in: {VALID_CONFIDENCE_LEVELS}")
        return confidence

    @field_validator("scenario")
    def __valid_scenario(cls, scenario: str) -> str:
        if not scenario in VALID_SCENARIOS:
            raise ValueError(f"scenario must be in: {VALID_SCENARIOS}")
        return scenario

    def __post_init__(self) -> None:
        self.forecast = Forecast(data=self.data)

    @staticmethod
    def __check_format(expected_format: str, path: str) -> None:
        provided_format = str(path).split(".")[-1]
        assert (
            provided_format == expected_format
        ), f"the file format must be '.{expected_format}', not '.{provided_format}'"

    @staticmethod
    def load(confidence: str, scenario: str) -> SLP:
        slp = json.loads(requests.get(SCENARIO_FILES[confidence][scenario]).text)
        return SLP(
            confidence=slp["confidence"],
            scenario=slp["scenario"],
            metadata=Metadata(
                description=slp["metadata"]["description"],
                reference=ReferenceLinks(
                    wiki=slp["metadata"]["reference"]["wiki"],
                    doi=slp["metadata"]["reference"]["doi"],
                ),
                download=DownloadLinks(
                    dataset=slp["metadata"]["download"]["dataset"],
                    raw=slp["metadata"]["download"]["raw"],
                    ssp=slp["metadata"]["download"]["ssp"],
                ),
            ),
            data=Data(_json=slp["data"]),
        )

    @staticmethod
    def save(path: str):
        SLP.__check_format("ssp", str(path))
        raise
