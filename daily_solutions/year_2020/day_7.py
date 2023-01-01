import re
from collections import defaultdict
from typing import Any, Iterable, Set, Tuple

from daily_solutions.base import BaseDailySolution

"""
You land at the regional airport in time for your next flight. In fact, it looks like
you'll even have time to grab some food: all flights are currently delayed due to
issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced
about bags and their contents; bags must be color-coded and must contain specific
quantities of other color-coded bags. Apparently, nobody responsible for these
regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded
blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted
black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how
many different bag colors would be valid for the outermost bag? (In other words: how
many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

1. A bright white bag, which can hold your shiny gold bag directly.
2. A muted yellow bag, which can hold your shiny gold bag directly, plus some other
   bags.
3. A dark orange bag, which can hold bright white and muted yellow bags, either of which
   could then hold your shiny gold bag.
4. A light red bag, which can hold bright white and muted yellow bags, either of which
   could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one
shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of
rules is quite long; make sure you get all of it.)

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but
because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it)
plus 2 vibrant plum bags (and the 11 bags within each of those):
1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than
this example; be sure to count all of the bags, even if the nesting becomes
topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""


def parse_edge_tuples(rule_str: str) -> Tuple[str, list[Tuple[str, int]]]:
    regex_parent_pattern = r"([a-z]+ [a-z]+) bags contain"
    regex_child_pattern = r"[0-9]+ [a-z]+ [a-z]+"

    parent = re.match(regex_parent_pattern, rule_str).groups()[0]
    children_raw = re.findall(regex_child_pattern, rule_str)
    if len(children_raw) == 0:
        return parent, []

    children = []
    for child_str in children_raw:
        count, desc, color = child_str.split(" ")
        children.append((f"{desc} {color}", int(count)))

    return parent, children


def build_graph_from_edge_tuples(
    edge_tuples: Iterable[Tuple[str, list[Tuple[str, int]]]]
) -> dict[str, Set[str]]:
    color_graph = defaultdict(set)
    for parent, child_list in edge_tuples:
        for name, count in child_list:
            color_graph[name].add(parent)
    return color_graph


def bfs_step_part_1(
    graph: dict[str, Set[str]], parent: str, visited: Set[str]
) -> Set[str]:
    visited.add(parent)
    children = graph.get(parent, {})
    for child in children:
        visited.update(bfs_step_part_1(graph, child, visited))
    return visited


def bfs_step_part_2(graph: dict[str, Set[str]], parent: str) -> int:
    children = graph.get(parent, {})
    if len(children) == 0:
        return 0
    else:
        return sum(
            [
                count + (count * bfs_step_part_2(graph, name))
                for (name, count) in children
            ]
        )


class Year2020Day7Solution(BaseDailySolution):
    YEAR = 2020
    DAY = 7

    @classmethod
    def format_data(
        cls, input_data: list[str]
    ) -> list[Tuple[str, list[Tuple[str, int]]]]:
        return list(map(parse_edge_tuples, input_data))

    @classmethod
    def solve_part_1(cls, edge_tuples: list[Tuple[str, list[Tuple[str, int]]]]) -> int:
        color_graph = build_graph_from_edge_tuples(edge_tuples)
        return len(bfs_step_part_1(color_graph, "shiny gold", set())) - 1

    @classmethod
    def solve_part_2(cls, edge_tuples: list[Tuple[str, list[Tuple[str, int]]]]) -> Any:
        color_graph = {k: set(v) for (k, v) in edge_tuples}
        return bfs_step_part_2(color_graph, "shiny gold")
