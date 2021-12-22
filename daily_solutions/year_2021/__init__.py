from typing import Callable, Dict

from daily_solutions.year_2021.day_1 import Year2021Day1Solution
from daily_solutions.year_2021.day_2 import Year2021Day2Solution
from daily_solutions.year_2021.day_3 import Year2021Day3Solution
from daily_solutions.year_2021.day_4 import Year2021Day4Solution
from daily_solutions.year_2021.day_5 import Year2021Day5Solution
from daily_solutions.year_2021.day_6 import Year2021Day6Solution
from daily_solutions.year_2021.day_7 import Year2021Day7Solution
from daily_solutions.year_2021.day_8 import Year2021Day8Solution
from daily_solutions.year_2021.day_9 import Year2021Day9Solution

DAYS_TO_SOLUTIONS: Dict[str, Callable] = {
    "1": Year2021Day1Solution,
    "2": Year2021Day2Solution,
    "3": Year2021Day3Solution,
    "4": Year2021Day4Solution,
    "5": Year2021Day5Solution,
    "6": Year2021Day6Solution,
    "7": Year2021Day7Solution,
    "8": Year2021Day8Solution,
    "9": Year2021Day9Solution,
}
