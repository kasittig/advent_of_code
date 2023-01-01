from typing import Callable

from daily_solutions.year_2020 import DAYS_TO_SOLUTIONS as solutions_2020
from daily_solutions.year_2021 import DAYS_TO_SOLUTIONS as solutions_2021
from daily_solutions.year_2022 import DAYS_TO_SOLUTIONS as solutions_2022

SOLUTIONS_BY_YEAR: dict[str, dict[str, Callable]] = {
    "2022": solutions_2022,
    "2021": solutions_2021,
    "2020": solutions_2020,
}
DEFAULT_YEAR = "2022"
