from unittest import TestCase

from daily_solutions.year_2021.day_8 import (
    Year2021Day8Solution,
    get_initial_mappings,
    get_translation_table_from_input,
    solve_translation_table,
    translate_entry,
    translate_parsed_line,
)

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


class Day8SolutionTestCase(TestCase):
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
        self.assertEqual(61229, self.solution.solve_part_2(formatted_example))


class Day8HelpersTestCase(TestCase):
    def setUp(self) -> None:
        self.data = [
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
        ]

    def test_get_initial_mappings(self) -> None:
        initial_table = get_initial_mappings(self.data)

        for (number, options) in [
            (0, ["cbdgef", "fgaecd", "agebfd"]),
            (1, ["be"]),
            (2, ["fdcge", "fecdb", "fabcd"]),
            (3, ["fdcge", "fecdb", "fabcd"]),
            (4, ["cgeb"]),
            (5, ["fdcge", "fecdb", "fabcd"]),
            (6, ["cbdgef", "fgaecd", "agebfd"]),
            (7, ["edb"]),
            (8, ["cfbegad"]),
            (9, ["cbdgef", "fgaecd", "agebfd"]),
        ]:
            with self.subTest(f"Number: {number}, Options: {options}"):
                self.assertEqual(options, initial_table[number])

    def test_solve_translation_table(self) -> None:
        initial_table = get_initial_mappings(self.data)
        translation_table = solve_translation_table(initial_table)

        for (number, options) in [
            (0, "agebfd"),
            (1, "be"),
            (2, "fabcd"),
            (3, "fecdb"),
            (4, "cgeb"),
            (5, "fdcge"),
            (6, "fgaecd"),
            (7, "edb"),
            (8, "cfbegad"),
            (9, "cbdgef"),
        ]:
            with self.subTest(f"Number: {number}, Options: {options}"):
                self.assertEqual(options, translation_table[number])

    def test_translate_entry(self) -> None:
        tt = get_translation_table_from_input(self.data)
        self.assertEqual(8, translate_entry("fdgacbe", tt))
        self.assertEqual(3, translate_entry("cefdb", tt))
        self.assertEqual(9, translate_entry("cefbgd", tt))
        self.assertEqual(4, translate_entry("gcbe", tt))

    def test_translate_parsed_line(self) -> None:
        self.assertEqual(
            8394,
            translate_parsed_line((self.data, ["fdgacbe", "cefdb", "cefbgd", "gcbe"])),
        )
