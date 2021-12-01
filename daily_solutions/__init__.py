from typing import Callable, Dict

from daily_solutions.year_2020 import DAYS_TO_SOLUTIONS as solutions_2020
from daily_solutions.year_2021 import DAYS_TO_SOLUTIONS as solutions_2021

SOLUTIONS_BY_YEAR: Dict[str, Dict[str, Callable]] = {
    "2021": solutions_2021,
    "2020": solutions_2020,
}
DEFAULT_YEAR = "2021"
