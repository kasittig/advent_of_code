from unittest import TestCase

from daily_solutions.year_2021.day_5 import Year2021Day5Solution

example_coords = [
    ((0, 9), (5, 9)),
    ((8, 0), (0, 8)),
    ((9, 4), (3, 4)),
    ((2, 2), (2, 1)),
    ((7, 0), (7, 4)),
    ((6, 4), (2, 0)),
    ((0, 9), (2, 9)),
    ((3, 4), (1, 4)),
    ((0, 0), (8, 8)),
    ((5, 5), (8, 2)),
]


class Day5TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day5Solution

    def test_format_data(self) -> None:
        self.assertEqual(
            [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4))],
            self.solution.format_data(["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4"]),
        )

    def test_solve_part_1(self) -> None:
        self.assertEqual(self.solution.solve_part_1(example_coords), 5)

    def test_solve_part_2(self) -> None:
        self.assertEqual(self.solution.solve_part_2(example_coords), 12)
