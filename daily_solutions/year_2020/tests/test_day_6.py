from unittest import TestCase

from daily_solutions.year_2020.day_6 import Year2020Day6Solution, split_by_groups

example = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]
grouped_example = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]


class Day6TestCase(TestCase):
    def test_split_by_groups(self) -> None:
        self.assertEqual(grouped_example, split_by_groups(example))

    def test_solve_part_1(self) -> None:
        self.assertEqual(11, Year2020Day6Solution().solve_part_1(grouped_example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(6, Year2020Day6Solution().solve_part_2(grouped_example))
