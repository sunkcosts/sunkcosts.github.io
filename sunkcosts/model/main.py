# from sunklib.model.premise import Premise
# from dataclasses import dataclass
# from typing import Callable


# class Context:
#     pass


# def assume_static_value(ctx: Context) -> float:
#     pass


# @dataclass
# class Premises:
#     cost_of_human_life: Callable


from pydantic import field_validator
from pydantic.dataclasses import dataclass

from sunkcosts.model.ar6 import VALID_SCENARIOS


@dataclass
class ModelOutcome:
    pass


@dataclass
class SunkCostsModel:
    """
    Miami sea level rise economic cost forecast model.

    Args:
        ssp_scenario (str): _description_
        ipcc_arc_confidence (str): _description_
        regional_modifier (bool): _description_
        monetary_value_of_human_life (float): _description_
    """

    ssp_scenario: str = "245"
    ipcc_arc_confidence: str = "medium"
    regional_modifier: float = 1
    monetary_value_of_human_life: float = 7_500_000

    @field_validator("ssp_scenario")
    def __validate_ssp_scenario(cls, ssp_scenario: str) -> str:
        if not ssp_scenario in VALID_SCENARIOS:
            raise ValueError(f"scenario must be in: {VALID_SCENARIOS}")
        return ssp_scenario

    def __post_init__(self):
        self.__outcome: ModelOutcome | None = None

    @property
    def outcome(self) -> ModelOutcome:
        if self.__outcome is None:
            raise Exception("the model has not yet been run")
        else:
            return self.__outcome

    def run(self, n: int) -> bool:
        """_summary_

        Args:
            n (int): number of times to run model
        """
        # model code
        return True
