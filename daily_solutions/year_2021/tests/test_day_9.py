from unittest import TestCase

from daily_solutions.year_2021.day_9 import HeightMap, Year2021Day9Solution

example = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

formatted_example = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]


class Day9TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day9Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(15, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(1134, self.solution.solve_part_2(self.data))


class HeightMapTestCase(TestCase):
    def setUp(self) -> None:
        self.heightmap = HeightMap(formatted_example)

    def test_get_all_low_points(self) -> None:
        self.assertEqual(4, len(self.heightmap.get_all_low_points()))
