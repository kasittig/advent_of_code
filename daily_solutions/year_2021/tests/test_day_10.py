from unittest import TestCase

from daily_solutions.year_2021.day_10 import (
    Year2021Day10Solution,
    correct_entry,
    score_entry,
    validate_entry,
)

entries = [
    ("[({(<(())[]>[[{[]{<()<>>", True),
    ("[(()[<>])]({[<{<<[]>>(", True),
    ("(((({<>}<{<{<>}{[]{[]{}", True),
    ("{<[[]]>}<{[{[{[]{()[[[]", True),
    ("<{([{{}}[<[[[<>{}]]]>[]]", True),
    ("{([(<{}[<>[]}>{[]{[(<()>", False),
    ("[[<[([]))<([[{}[[()]]]", False),
    ("[{[{({}]{}}([{[{{{}}([]", False),
    ("[<(<(<(<{}))><([]([]()", False),
    ("<{([([[(<>()){}]>(<<{{", False),
]

corrections = [
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
    ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
    ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
]

scored_corrections = [
    ("[({(<(())[]>[[{[]{<()<>>", 288957),
    ("[(()[<>])]({[<{<<[]>>(", 5566),
    ("(((({<>}<{<{<>}{[]{[]{}", 1480781),
    ("{<[[]]>}<{[{[{[]{()[[[]", 995444),
    ("<{([{{}}[<[[[<>{}]]]>[]]", 294),
]


class Day10SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day10Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(26397, self.solution.solve_part_1([e for e, _ in entries]))

    def test_solve_part_2(self) -> None:
        self.assertEqual(
            288957, self.solution.solve_part_2([e for e, valid in entries if valid])
        )


class Day10HelpersTestCase(TestCase):
    def test_validate_entry(self) -> None:
        for (entry, expected) in entries:
            with self.subTest(entry=entry):
                self.assertEqual(expected, validate_entry(entry)[0])

    def test_correct_entry(self) -> None:
        for (entry, expected) in corrections:
            with self.subTest(entry=entry):
                self.assertEqual(expected, correct_entry(entry))

    def test_score_entry(self) -> None:
        for (entry, expected) in scored_corrections:
            with self.subTest(entry=entry):
                self.assertEqual(expected, score_entry(entry))
