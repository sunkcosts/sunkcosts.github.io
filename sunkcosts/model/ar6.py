from __future__ import annotations

from pathlib import Path
from pydantic import BaseModel, field_validator
from netCDF4._netCDF4 import Dataset as NCD

VALID_CONFIDENCE_LEVELS = {"medium", "high"}
VALID_SCENARIOS = {"ssp126", "ssp245", "ssp585"}


class AR6SeaLevelProjection(BaseModel):
    """
    Derived from ar6/global/confidence_output_files.
    """

    confidence: str
    scenario: str

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

    @staticmethod
    def load_raw(
        basepath: str | Path, confidence: str, scenario: str
    ) -> AR6SeaLevelProjection:
        datapath = Path(
            f"{str(basepath)}/{confidence}_confidence/{scenario}/total_{scenario}_{confidence}_confidence_values.nc"
        )
        raise

    @staticmethod
    def load(confidence: str, scenario: str) -> AR6SeaLevelProjection:
        raise
