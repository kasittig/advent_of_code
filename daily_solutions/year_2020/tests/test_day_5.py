from unittest import TestCase

from daily_solutions.year_2020.day_5 import parse_seat_id


class Day5TestCase(TestCase):
    def test_parse_row_column(self) -> None:
        self.assertEqual(567, parse_seat_id("BFFFBBFRRR"))
