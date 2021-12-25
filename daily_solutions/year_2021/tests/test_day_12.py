from unittest import TestCase

from daily_solutions.year_2021.day_12 import Year2021Day12Solution

example_1 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

example_1_edge_dict = {
    "dc": ["end", "start", "HN", "LN", "kj"],
    "end": ["dc", "HN"],
    "HN": ["start", "dc", "end", "kj"],
    "start": ["HN", "kj", "dc"],
    "kj": ["start", "sa", "HN", "dc"],
    "LN": ["dc"],
    "sa": ["kj"],
}


class Day12SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day12Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(
            19, self.solution.solve_part_1(self.solution.format_data(example_1))
        )

    def test_solve_part_2(self) -> None:
        self.assertEqual(
            103, self.solution.solve_part_2(self.solution.format_data(example_1))
        )
