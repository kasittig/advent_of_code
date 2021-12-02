from typing import Callable, Dict

from daily_solutions.year_2020.day_1 import Year2020Day1Solution
from daily_solutions.year_2020.day_2 import Year2020Day2Solution
from daily_solutions.year_2020.day_3 import Year2020Day3Solution
from daily_solutions.year_2020.day_4 import Year2020Day4Solution
from daily_solutions.year_2020.day_5 import Year2020Day5Solution
from daily_solutions.year_2020.day_6 import Year2020Day6Solution

DAYS_TO_SOLUTIONS: Dict[str, Callable] = {
    "1": Year2020Day1Solution,
    "2": Year2020Day2Solution,
    "3": Year2020Day3Solution,
    "4": Year2020Day4Solution,
    "5": Year2020Day5Solution,
    "6": Year2020Day6Solution,
}
