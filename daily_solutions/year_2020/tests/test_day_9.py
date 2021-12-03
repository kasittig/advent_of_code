from unittest import TestCase

from daily_solutions.year_2020.day_9 import (
    check_encoding,
    find_window_sums_to_target,
    is_window_valid,
)

example = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


class Day9TestCase(TestCase):
    def test_check_sum_in_window(self) -> None:
        self.assertTrue(is_window_valid([35, 20, 15, 25, 47, 40]))
        self.assertTrue(is_window_valid([20, 15, 25, 47, 40, 62]))
        self.assertTrue(is_window_valid([15, 25, 47, 40, 62, 55]))
        self.assertFalse(is_window_valid([95, 102, 117, 150, 182, 127]))

    def test_check_encoding(self) -> None:
        self.assertEqual(127, check_encoding(example, 5))

    def test_find_window_sums_to_target(self) -> None:
        self.assertEqual((15, 47), find_window_sums_to_target(example, 127))
