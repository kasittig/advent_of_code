from typing import Callable, Dict

from daily_solutions.year_2020.day_1 import solve_day_1
from daily_solutions.year_2020.day_2 import solve_day_2
from daily_solutions.year_2020.day_3 import solve_day_3
from daily_solutions.year_2020.day_4 import solve_day_4

DAYS_TO_SOLUTIONS: Dict[str, Callable] = {
    "1": solve_day_1,
    "2": solve_day_2,
    "3": solve_day_3,
    "4": solve_day_4,
}
