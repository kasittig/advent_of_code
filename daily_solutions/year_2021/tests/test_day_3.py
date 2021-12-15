from unittest import TestCase

from daily_solutions.year_2021.day_3 import (
    count_bits,
    find_epsilon_gamma_rates,
    find_oxygen_co2_rates,
)

example = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


class Day3TestCase(TestCase):
    def test_count_bits(self):
        counts = count_bits(example)
        self.assertEqual(counts, [2, -2, 4, 2, -2])

    def test_epsilon_gamma(self):
        epsilon, gamma = find_epsilon_gamma_rates(example)
        self.assertEqual(epsilon, "01001")
        self.assertEqual(gamma, "10110")

    def test_oxygen_co2(self):
        oxygen, co2 = find_oxygen_co2_rates(example)
        self.assertEqual(oxygen, "10111")
        self.assertEqual(co2, "01010")
