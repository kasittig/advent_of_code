from unittest import TestCase

from core.utils import get_frequency_counts
from daily_solutions.year_2021.day_6 import Year2021Day6Solution, do_step

initial = [3, 4, 3, 1, 2]
day_1 = [2, 3, 2, 0, 1]
day_2 = [1, 2, 1, 6, 0, 8]
day_3 = [0, 1, 0, 5, 6, 7, 8]
day_18 = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]


class Day6TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day6Solution
        self.initial = get_frequency_counts(initial)

    def test_do_step(self) -> None:
        self.assertEqual({2: 2, 3: 1, 0: 1, 1: 1}, do_step(self.initial))
        self.assertEqual(
            {1: 2, 2: 1, 6: 1, 0: 1, 8: 1}, do_step({2: 2, 3: 1, 0: 1, 1: 1})
        )
        self.assertEqual(
            {0: 2, 1: 1, 5: 1, 6: 1, 7: 1, 8: 1},
            do_step({1: 2, 2: 1, 6: 1, 0: 1, 8: 1}),
        )

    def test_solve_part_1(self) -> None:
        self.assertEqual(5934, self.solution.solve_part_1(self.initial))

    def test_solve_part_2(self) -> None:
        self.assertEqual(26984457539, self.solution.solve_part_2(self.initial))
