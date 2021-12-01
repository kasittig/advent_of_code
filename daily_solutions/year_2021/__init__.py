from typing import Callable

from daily_solutions.year_2021.day_1 import solve_day_1
from frozendict import frozendict

DAYS_TO_SOLUTIONS: frozendict[str, Callable] = frozendict({"1": solve_day_1})
