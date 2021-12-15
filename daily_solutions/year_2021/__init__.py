from typing import Callable, Dict

from daily_solutions.year_2021.day_1 import Year2021Day1Solution
from daily_solutions.year_2021.day_2 import Year2021Day2Solution
from daily_solutions.year_2021.day_3 import Year2021Day3Solution

DAYS_TO_SOLUTIONS: Dict[str, Callable] = {
    "1": Year2021Day1Solution,
    "2": Year2021Day2Solution,
    "3": Year2021Day3Solution,
}
