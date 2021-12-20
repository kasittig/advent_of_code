from unittest import TestCase

from daily_solutions.year_2021.day_8 import Year2021Day8Solution

example = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

formatted_example = [
    (
        [
            "be",
            "cfbegad",
            "cbdgef",
            "fgaecd",
            "cgeb",
            "fdcge",
            "agebfd",
            "fecdb",
            "fabcd",
            "edb",
        ],
        ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
    ),
    (
        [
            "edbfga",
            "begcd",
            "cbg",
            "gc",
            "gcadebf",
            "fbgde",
            "acbgfd",
            "abcde",
            "gfcbed",
            "gfec",
        ],
        ["fcgedb", "cgb", "dgebacf", "gc"],
    ),
    (
        [
            "fgaebd",
            "cg",
            "bdaec",
            "gdafb",
            "agbcfd",
            "gdcbef",
            "bgcad",
            "gfac",
            "gcb",
            "cdgabef",
        ],
        ["cg", "cg", "fdcagb", "cbg"],
    ),
    (
        [
            "fbegcd",
            "cbd",
            "adcefb",
            "dageb",
            "afcb",
            "bc",
            "aefdc",
            "ecdab",
            "fgdeca",
            "fcdbega",
        ],
        ["efabcd", "cedba", "gadfec", "cb"],
    ),
    (
        [
            "aecbfdg",
            "fbg",
            "gf",
            "bafeg",
            "dbefa",
            "fcge",
            "gcbea",
            "fcaegb",
            "dgceab",
            "fcbdga",
        ],
        ["gecf", "egdcabf", "bgf", "bfgea"],
    ),
    (
        [
            "fgeab",
            "ca",
            "afcebg",
            "bdacfeg",
            "cfaedg",
            "gcfdb",
            "baec",
            "bfadeg",
            "bafgc",
            "acf",
        ],
        ["gebdcfa", "ecba", "ca", "fadegcb"],
    ),
    (
        [
            "dbcfg",
            "fgd",
            "bdegcaf",
            "fgec",
            "aegbdf",
            "ecdfab",
            "fbedc",
            "dacgb",
            "gdcebf",
            "gf",
        ],
        ["cefg", "dcbef", "fcge", "gbcadfe"],
    ),
    (
        [
            "bdfegc",
            "cbegaf",
            "gecbf",
            "dfcage",
            "bdacg",
            "ed",
            "bedf",
            "ced",
            "adcbefg",
            "gebcd",
        ],
        ["ed", "bcgafe", "cdgba", "cbgef"],
    ),
    (
        [
            "egadfb",
            "cdbfeg",
            "cegd",
            "fecab",
            "cgb",
            "gbdefca",
            "cg",
            "fgcdab",
            "egfdb",
            "bfceg",
        ],
        ["gbdfcae", "bgc", "cg", "cgb"],
    ),
    (
        [
            "gcafb",
            "gcf",
            "dcaebfg",
            "ecagb",
            "gf",
            "abcdeg",
            "gaef",
            "cafbge",
            "fdbac",
            "fegbdc",
        ],
        ["fgae", "cfgab", "fg", "bagce"],
    ),
]


class Day8TestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day8Solution

    def test_format_data(self) -> None:
        result = self.solution.format_data(example)

        for i in range(len(result)):
            with self.subTest(i=i):
                self.assertEqual(formatted_example[i], result[i])

    def test_solve_part_1(self) -> None:
        self.assertEqual(26, self.solution.solve_part_1(formatted_example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(0, self.solution.solve_part_2(formatted_example))
