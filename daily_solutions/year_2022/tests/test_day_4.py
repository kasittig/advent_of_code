from unittest import TestCase

from daily_solutions.year_2022.day_4 import Year2022Day4Solution

example = []


class Day4SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2022Day4Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(None, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day4HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
