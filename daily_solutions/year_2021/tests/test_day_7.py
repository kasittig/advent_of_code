from unittest import TestCase

from daily_solutions.year_2021.day_7 import Year2021Day7Solution

example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class Day7TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day7Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(37, self.solution.solve_part_1(example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(168, self.solution.solve_part_2(example))
