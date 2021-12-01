from typing import Callable, Dict

from daily_solutions.year_2020.day_1 import Year2020Day1Solution
from daily_solutions.year_2020.day_2 import Year2020Day2Solution
from daily_solutions.year_2020.day_3 import Year2020Day3Solution
from daily_solutions.year_2020.day_4 import Year2020Day4Solution

DAYS_TO_SOLUTIONS: Dict[str, Callable] = {
    "1": Year2020Day1Solution,
    "2": Year2020Day2Solution,
    "3": Year2020Day3Solution,
    "4": Year2020Day4Solution,
}
