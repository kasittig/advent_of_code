from unittest import TestCase

from daily_solutions.year_2021.day_14 import (
    Year2021Day14Solution,
    count_polymer_bases,
    do_step,
)

example = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

example_rules = {
    "CH": ["CB", "BH"],
    "HH": ["HN", "NH"],
    "CB": ["CH", "HB"],
    "NH": ["NC", "CH"],
    "HB": ["HC", "CB"],
    "HC": ["HB", "BC"],
    "HN": ["HC", "CN"],
    "NN": ["NC", "CN"],
    "BH": ["BH", "HH"],
    "NC": ["NB", "BC"],
    "NB": ["NB", "BB"],
    "BN": ["BB", "BN"],
    "BB": ["BN", "NB"],
    "BC": ["BB", "BC"],
    "CC": ["CN", "NC"],
    "CN": ["CC", "CN"],
}


class Day14SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day14Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(1588, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(2188189693529, self.solution.solve_part_2(self.data))


class Day14HelpersTestCase(TestCase):
    def test_do_step(self) -> None:
        # NNCB -> NCNBCHB
        # [NC, CN, NB, BC, CH, HB]
        self.assertEqual(
            do_step({"NN": 1, "NC": 1, "CB": 1}, example_rules),
            {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1},
        )
        # NCNBCHB -> NBCCNBBBCBHCB
        # [NB, BC, CC, CN, NB, BB, BB, BC, CB, BH, CB]
        self.assertEqual(
            do_step(
                {"NC": 1, "CN": 1, "NB": 1, "BC": 1, "CH": 1, "HB": 1}, example_rules
            ),
            {
                "BC": 2,
                "CC": 1,
                "CN": 1,
                "NB": 2,
                "BB": 2,
                "CB": 2,
                "BH": 1,
                "HC": 1,
            },
        )

    def test_count_polymer_bases(self) -> None:
        self.assertEqual(
            {"B": 11, "C": 8, "N": 3, "H": 2},
            count_polymer_bases(
                {
                    "BC": 2,
                    "CC": 1,
                    "CN": 1,
                    "NB": 2,
                    "BB": 2,
                    "CB": 2,
                    "BH": 1,
                    "HC": 1,
                }
            ),
        )
