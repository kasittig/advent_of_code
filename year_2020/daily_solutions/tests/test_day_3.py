from unittest import TestCase
from typing import List
from year_2020.daily_solutions.day_3 import count_trees, get_index, tree_at_idx, calc_part_2

example: List[str] = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


class Day3TestCase(TestCase):
    def test_count_trees(self) -> None:
        self.assertEqual(count_trees(example, 1), 2)
        self.assertEqual(count_trees(example), 7)
        self.assertEqual(count_trees(example, 3), 7)
        self.assertEqual(count_trees(example, 5), 3)
        self.assertEqual(count_trees(example, 7), 4)
        self.assertEqual(count_trees(example, 1, 2), 2)

    def test_get_index(self) -> None:
        self.assertEqual(get_index(0, 11), 0)
        self.assertEqual(get_index(1, 11), 3)
        self.assertEqual(get_index(2, 11), 6)
        self.assertEqual(get_index(3, 11), 9)
        self.assertEqual(get_index(4, 11), 1)
        self.assertEqual(get_index(5, 11), 4)

    def test_tree_at_idx(self) -> None:
        self.assertFalse(tree_at_idx(example[0], 0))
        self.assertFalse(tree_at_idx(example[1], 3))
        self.assertTrue(tree_at_idx(example[2], 6))
        self.assertFalse(tree_at_idx(example[3], 9))
        self.assertTrue(tree_at_idx(example[4], 1))
        self.assertTrue(tree_at_idx(example[5], 4))

    def test_calc_part_two(self) -> None:
        self.assertEqual(calc_part_2(example), 336)


