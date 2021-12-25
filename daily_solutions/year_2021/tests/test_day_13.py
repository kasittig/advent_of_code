from unittest import TestCase

from daily_solutions.year_2021.day_13 import Year2021Day13Solution


example = []


class Day13SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day13Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(0, self.solution.solve_part_1(example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(example))


class Day13HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
