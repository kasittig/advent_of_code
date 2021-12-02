from unittest import TestCase

from daily_solutions.year_2020.day_5 import parse_row_column


class Day5TestCase(TestCase):
    def test_parse_row_column(self) -> None:
        self.assertEqual((70, 7), parse_row_column("BFFFBBFRRR"))
