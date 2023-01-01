from unittest import TestCase

from daily_solutions.year_2022.day_2 import Year2022Day2Solution

example = ["A Y", "B X", "C Z"]


class Day2SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2022Day2Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(15, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(12, self.solution.solve_part_2(self.data))


class Day2HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
