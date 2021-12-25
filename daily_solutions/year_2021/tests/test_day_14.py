from unittest import TestCase

from daily_solutions.year_2021.day_14 import Year2021Day14Solution


example = []


class Day14SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day14Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(0, self.solution.solve_part_1(example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(example))


class Day14HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
