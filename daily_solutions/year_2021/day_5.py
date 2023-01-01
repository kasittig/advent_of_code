import re
from collections import defaultdict
from typing import Any, Tuple

from daily_solutions.base import BaseDailySolution

"""
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds,
so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you
to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end
the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends.
In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of
lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 ->
2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the
above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also
consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal,
vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still
anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""


class VentGrid(object):
    def __init__(self):
        self.vent_grid = defaultdict(lambda: defaultdict(int))

    def add_vent(
        self, start: Tuple[int, int], end: Tuple[int, int], diagonals: bool = False
    ) -> None:
        x_step = int(
            0
            if end[0] - start[0] == 0
            else (end[0] - start[0]) / (abs(end[0] - start[0]))
        )
        y_step = int(
            0
            if end[1] - start[1] == 0
            else (end[1] - start[1]) / (abs(end[1] - start[1]))
        )

        if x_step != 0 and y_step != 0 and not diagonals:
            return

        x = start[0]
        y = start[1]

        while x != end[0] or y != end[1]:
            self.vent_grid[x][y] += 1
            x += x_step
            y += y_step
        self.vent_grid[x][y] += 1


class Year2021Day5Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 5

    @classmethod
    def format_data(
        cls, input_data: list[str]
    ) -> list[Tuple[Tuple[int, int], Tuple[int, int]]]:
        regex_pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
        coordinates: list[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        for entry in input_data:
            m = re.match(regex_pattern, entry).groups()
            start = (int(m[0]), int(m[1]))
            end = (int(m[2]), int(m[3]))
            coordinates.append((start, end))
        return coordinates

    @classmethod
    def solve_part_1(
        cls, input_data: list[Tuple[Tuple[int, int], Tuple[int, int]]]
    ) -> int:
        vg = VentGrid()
        for start, end in input_data:
            vg.add_vent(start, end)

        return sum(
            [
                1
                for column in vg.vent_grid.values()
                for value in column.values()
                if value > 1
            ]
        )

    @classmethod
    def solve_part_2(cls, input_data: Any) -> Any:
        vg = VentGrid()
        for start, end in input_data:
            vg.add_vent(start, end, diagonals=True)

        return sum(
            [
                1
                for column in vg.vent_grid.values()
                for value in column.values()
                if value > 1
            ]
        )
