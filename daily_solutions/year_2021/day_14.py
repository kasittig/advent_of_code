from collections import defaultdict
from math import ceil
from typing import Any, Dict, List, Tuple

from daily_solutions.base import BaseDailySolution

"""
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization
equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves
should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer
template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result
after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are
immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all
pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs
1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common
element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What
do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair
insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H
(occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What
do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""


def do_step(
    polymer: Dict[str, int], instruction_dict: Dict[str, Tuple[str, str]]
) -> Dict[str, int]:
    new_polymer: Dict[str, int] = defaultdict(int)
    for (pair, frequency) in polymer.items():
        (new1, new2) = instruction_dict[pair]
        new_polymer[new1] += frequency
        new_polymer[new2] += frequency
    return new_polymer


def do_n_steps(
    polymer: Dict[str, int], instruction_dict: Dict[str, Tuple[str, str]], n: int
) -> Dict[str, int]:
    for i in range(n):
        polymer = do_step(polymer, instruction_dict)
    return polymer


def count_polymer_bases(polymer: Dict[str, int]) -> Dict[str, int]:
    counts = defaultdict(int)
    for base_pair, count in polymer.items():
        counts[base_pair[0]] += count
        counts[base_pair[1]] += count
    return counts


class Year2021Day14Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 14

    @classmethod
    def format_data(
        cls, input_data: List[str]
    ) -> Tuple[str, Dict[str, int], Dict[str, Tuple[str, str]]]:
        initial = input_data[0].strip()
        initial_dict = defaultdict(int)
        for i in range(len(initial) - 1):
            initial_dict[initial[i : i + 2]] += 1

        instruction_dict: Dict[str, Tuple[str, str]] = {}
        instructions = [
            instruction.strip().split(" -> ") for instruction in input_data[2:]
        ]
        for base_pair, result in instructions:
            base1 = base_pair[0]
            base2 = base_pair[1]
            instruction_dict[base_pair] = (base1 + result, result + base2)
        return initial, initial_dict, instruction_dict

    @classmethod
    def solve_part_1(
        cls, input_data: Tuple[str, Dict[str, int], Dict[str, Tuple[str, str]]]
    ) -> int:
        template, polymer, instructions = input_data

        polymer = do_n_steps(polymer, instructions, 10)
        polymer_counts = count_polymer_bases(polymer)

        # Every base should appear in two pairs, except for the start and end pairs, so add these pairs back in
        polymer_counts[template[0]] += 1
        polymer_counts[template[-1]] += 1

        return int(max(polymer_counts.values()) / 2) - int(
            min(polymer_counts.values()) / 2
        )

    @classmethod
    def solve_part_2(
        cls, input_data: Tuple[str, Dict[str, int], Dict[str, Tuple[str, str]]]
    ) -> int:
        template, polymer, instructions = input_data

        polymer = do_n_steps(polymer, instructions, 40)
        polymer_counts = count_polymer_bases(polymer)

        # Every base should appear in two pairs, except for the start and end pairs, so add these pairs back in
        polymer_counts[template[0]] += 1
        polymer_counts[template[-1]] += 1
        return int(max(polymer_counts.values()) / 2) - int(
            min(polymer_counts.values()) / 2
        )
