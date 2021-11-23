from unittest import TestCase
from daily_solutions.day_1 import target_in_list, get_target_number_pair, solve_part_2, solve_part_1


EXAMPLE_INPUT_LIST = [1721, 979, 366, 299, 675, 1456]


class TestDay1(TestCase):
    def test_target_in_list(self) -> None:
        self.assertTrue(target_in_list(1, [1, 2, 3]))
        self.assertFalse(target_in_list(4, [1, 2, 3]))
        self.assertFalse(target_in_list(1, []))

    def test_get_target_number_pair(self) -> None:
        self.assertEqual(get_target_number_pair([1, 2, 3], 3), (1, 2))
        self.assertEqual(get_target_number_pair([1, 2, 3], 6), (None, None))
        self.assertEqual(get_target_number_pair([1, 2, 3], 4), (1, 3))
        self.assertEqual(get_target_number_pair([1, 2, 3], 5), (2, 3))

    def test_part_1(self) -> None:
        self.assertEqual(solve_part_1(EXAMPLE_INPUT_LIST, 2020), (1721, 299))

    def test_part_2(self) -> None:
        self.assertEqual(solve_part_2(EXAMPLE_INPUT_LIST, 2020), (979, 366, 675))
