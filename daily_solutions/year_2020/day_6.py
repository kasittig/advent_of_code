from collections import defaultdict
from typing import Any

from daily_solutions.base import BaseDailySolution

"""
As your flight approaches the regional airport where you'll switch to a much larger
plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do
is identify the questions for which anyone in your group answers "yes". Since your
group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and
asks if you can help. For each of the people in their group, you write down the
questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and
z. (Duplicate answers to the same question don't count extra; each question counts at
most once.)

Another group asks for your help, then another, and eventually you've collected answers
from every group on the plane (your puzzle input). Each group's answers are separated
by a blank line, and within each group, each person's answers are on a single line. For
example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

1. The first group contains one person who answered "yes" to 3 questions: a, b, and c.
2. The second group contains three people; combined, they answered "yes" to 3
   questions: a, b, and c.
3. The third group contains two people; combined, they answered "yes" to 3 questions:
   a, b, and c.
4. The fourth group contains four people; combined, they answered "yes" to only 1
   question, a.
5. The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is
the sum of those counts?

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one
word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to
identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

1. In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and
   c.
2. In the second group, there is no question to which everyone answered "yes".
3. In the third group, everyone answered yes to only 1 question, a. Since some people
   did not answer "yes" to b or c, they don't count.
4. In the fourth group, everyone answered yes to only 1 question, a.
5. In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is
the sum of those counts?
"""


def split_by_groups(input_data: list[str]) -> list[list[str]]:
    all_groups: list[list[str]] = []
    curr_group: list[str] = []

    for line in input_data:
        line = line.strip()
        if line == "":
            all_groups.append(curr_group)
            curr_group = []
        else:
            curr_group.append(line)
    if len(curr_group) > 0:
        all_groups.append(curr_group)
    return all_groups


def count_group_answers(group: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = defaultdict(int)
    for entry in group:
        for question in entry:
            count_dict[question] += 1
    return count_dict


class Year2020Day6Solution(BaseDailySolution):
    YEAR = 2020
    DAY = 6

    @classmethod
    def format_data(cls, input_data: list[str]) -> list[list[str]]:
        return split_by_groups(input_data)

    @classmethod
    def solve_part_1(cls, grouped_data: list[list[str]]) -> int:
        total_count = 0
        for group in grouped_data:
            count_dict = count_group_answers(group)
            total_count += len(count_dict.keys())
        return total_count

    @classmethod
    def solve_part_2(cls, grouped_data: list[Any]) -> Any:
        total_count = 0
        for group in grouped_data:
            count_dict = count_group_answers(group)
            for value in count_dict.values():
                total_count += int(value == len(group))
        return total_count
