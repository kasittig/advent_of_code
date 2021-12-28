from unittest import TestCase

from daily_solutions.year_2021.day_16 import Year2021Day16Solution


example = []


class Day16SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day16Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(None, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day16HelpersTestCase(TestCase):
    def test_helper(self) -> None:
        pass
