from unittest import TestCase

from daily_solutions.year_2020.day_7 import (
    Year2020Day7Solution,
    bfs_step_part_1,
    bfs_step_part_2,
    build_graph_from_edge_tuples,
    parse_edge_tuples,
)

example_rules = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]
example_edge_tuples = [
    ("light red", [("bright white", 1), ("muted yellow", 2)]),
    ("dark orange", [("bright white", 3), ("muted yellow", 4)]),
    ("bright white", [("shiny gold", 1)]),
    ("muted yellow", [("shiny gold", 2), ("faded blue", 9)]),
    ("shiny gold", [("dark olive", 1), ("vibrant plum", 2)]),
    ("dark olive", [("faded blue", 3), ("dotted black", 4)]),
    ("vibrant plum", [("faded blue", 5), ("dotted black", 6)]),
    ("faded blue", []),
    ("dotted black", []),
]
example_rule_graph_part_1 = {
    "muted yellow": {"light red", "dark orange"},
    "bright white": {"light red", "dark orange"},
    "shiny gold": {"bright white", "muted yellow"},
    "faded blue": {"muted yellow", "dark olive", "vibrant plum"},
    "dark olive": {"shiny gold"},
    "vibrant plum": {"shiny gold"},
    "dotted black": {"dark olive", "vibrant plum"},
}

example_rule_graph_part_2 = {
    "light red": {("bright white", 1), ("muted yellow", 2)},
    "dark orange": {("bright white", 3), ("muted yellow", 4)},
    "bright white": {("shiny gold", 1)},
    "muted yellow": {("shiny gold", 2), ("faded blue", 9)},
    "shiny gold": {("dark olive", 1), ("vibrant plum", 2)},
    "dark olive": {("faded blue", 3), ("dotted black", 4)},
    "vibrant plum": {("faded blue", 5), ("dotted black", 6)},
}


class Day7TestCase(TestCase):
    def test_parse_edge_tuples(self) -> None:
        for i in range(len(example_rules)):
            with self.subTest(i=i):
                self.assertEqual(
                    example_edge_tuples[i], parse_edge_tuples(example_rules[i])
                )

    def test_build_graph_from_edge_tuples(self) -> None:
        edge_graph = build_graph_from_edge_tuples(example_edge_tuples)
        for k in example_rule_graph_part_1.keys():
            self.assertTrue(edge_graph[k] == example_rule_graph_part_1[k])

    def test_build_graph_part_2(self) -> None:
        edge_graph = {k: set(v) for (k, v) in example_edge_tuples}
        for k in example_rule_graph_part_2.keys():
            self.assertTrue(edge_graph[k] == example_rule_graph_part_2[k])

    def test_solve_part_1(self) -> None:
        self.assertEqual(4, Year2020Day7Solution().solve_part_1(example_edge_tuples))

    def test_solve_part_2(self) -> None:
        self.assertEqual(32, Year2020Day7Solution().solve_part_2(example_edge_tuples))

    def test_bfs_step_part_1(self) -> None:
        self.assertEqual(
            {"dark orange"},
            bfs_step_part_1(example_rule_graph_part_1, "dark orange", set()),
        )
        self.assertEqual(
            {"light red"},
            bfs_step_part_1(example_rule_graph_part_1, "light red", set()),
        )
        self.assertEqual(
            {"light red", "muted yellow", "dark orange"},
            bfs_step_part_1(example_rule_graph_part_1, "muted yellow", set()),
        )
        self.assertEqual(
            {"light red", "muted yellow", "dark orange", "shiny gold", "bright white"},
            bfs_step_part_1(example_rule_graph_part_1, "shiny gold", set()),
        )

    def test_bfs_step_part_2(self) -> None:
        self.assertEqual(
            0,
            bfs_step_part_2(example_rule_graph_part_2, "dotted black"),
        )
        self.assertEqual(
            0,
            bfs_step_part_2(example_rule_graph_part_2, "faded blue"),
        )
        self.assertEqual(
            7,
            bfs_step_part_2(example_rule_graph_part_2, "dark olive"),
        )
        self.assertEqual(
            11,
            bfs_step_part_2(example_rule_graph_part_2, "vibrant plum"),
        )
        self.assertEqual(
            32,
            bfs_step_part_2(example_rule_graph_part_2, "shiny gold"),
        )
