from typing import Callable

from daily_solutions.year_2022.day_1 import Year2022Day1Solution
from daily_solutions.year_2022.day_2 import Year2022Day2Solution
from daily_solutions.year_2022.day_3 import Year2022Day3Solution
from daily_solutions.year_2022.day_4 import Year2022Day4Solution

DAYS_TO_SOLUTIONS: dict[str, Callable] = {
    "1": Year2022Day1Solution,
    "2": Year2022Day2Solution,
    "3": Year2022Day3Solution,
    "4": Year2022Day4Solution,
}
