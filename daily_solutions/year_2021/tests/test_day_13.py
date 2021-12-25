from unittest import TestCase

from daily_solutions.year_2021.day_13 import (
    Year2021Day13Solution,
    fold_along_x,
    fold_along_y,
    generate_initial_array,
)

example = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

example_coords = [
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
]

example_initial = [
    [".", ".", ".", "#", ".", ".", "#", ".", ".", "#", "."],
    [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", "#", ".", "#", "#", "."],
    [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
]

example_instructions = [("y", 7), ("x", 5)]

first_fold = [
    ["#", ".", "#", "#", ".", ".", "#", ".", ".", "#", "."],
    ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", "#", ".", ".", "#", ".", "#", "#", "#"],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

second_fold = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#"],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
]


class Day13SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day13Solution
        self.data = self.solution.format_data(example)

    def test_format_data(self) -> None:
        array, instructions = self.data
        self.assertEqual(array, example_initial)
        self.assertEqual(instructions, example_instructions)

    def test_solve_part_1(self) -> None:
        self.assertEqual(17, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day13HelpersTestCase(TestCase):
    def test_generate_initial_array(self) -> None:
        self.assertEqual(example_initial, generate_initial_array(example_coords))

    def test_fold_along_y(self) -> None:
        self.assertEqual(first_fold, fold_along_y(7, example_initial))

    def test_fold_along_x(self) -> None:
        self.assertEqual(second_fold, fold_along_x(5, first_fold))
