from unittest import TestCase

from daily_solutions.year_2021.day_9 import Year2021Day9Solution


example = []


class Day9TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day9Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(0, self.solution.solve_part_1(example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(example))
