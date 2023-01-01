from unittest import TestCase

from daily_solutions.year_2022.day_1 import Year2022Day1Solution

example = []


class Day1SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2022Day1Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(None, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day1HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
