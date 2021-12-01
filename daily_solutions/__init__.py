from typing import Callable

from frozendict import frozendict

from daily_solutions.year_2020 import DAYS_TO_SOLUTIONS as solutions_2020
from daily_solutions.year_2021 import DAYS_TO_SOLUTIONS as solutions_2021

SOLUTIONS_BY_YEAR: frozendict[str, frozendict[str, Callable]] = frozendict(
    {"2021": solutions_2021, "2020": solutions_2020}
)
DEFAULT_YEAR = "2021"
