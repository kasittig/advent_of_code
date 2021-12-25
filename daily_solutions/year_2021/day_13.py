from typing import Any, List, Tuple

from daily_solutions.base import BaseDailySolution

"""
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so
you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open
it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and
includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value,
x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and
the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the
paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to
fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold
instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with
-):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is
complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is
complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just
below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the
example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital
letters.

What code do you use to activate the infrared thermal imaging camera system?
"""


def generate_initial_array(coords: List[Tuple[int, int]]) -> List[List[str]]:
    width = max([coord[0] for coord in coords])
    height = max([coord[1] for coord in coords])
    initial_array = [["." for _ in range(width + 1)] for _ in range(height + 1)]

    for (x, y) in coords:
        initial_array[y][x] = "#"

    return initial_array


def fold_along_y(value: int, sheet: List[List[str]]) -> List[List[str]]:
    first_half = sheet[0:value]
    second_half = sheet[value:]
    second_half.reverse()

    return [combine_lines(f, s) for (f, s) in zip(first_half, second_half)]


def fold_along_x(value: int, sheet: List[List[str]]) -> List[List[str]]:
    new_sheet = []
    for line in sheet:
        first_half = line[0:value]
        second_half = line[value:]
        second_half.reverse()
        new_sheet.append(combine_lines(first_half, second_half))
    return new_sheet


def combine_lines(first: List[str], second: List[str]) -> List[str]:
    new_line = []
    for i in range(len(first)):
        next_char = "#" if first[i] == "#" or second[i] == "#" else "."
        new_line.append(next_char)
    return new_line


def fold_sheet(sheet: List[List[str]], instruction: Tuple[str, int]) -> List[List[str]]:
    axis, value = instruction
    if axis == "x":
        return fold_along_x(value, sheet)
    else:
        return fold_along_y(value, sheet)


class Year2021Day13Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 13

    @classmethod
    def format_data(
        cls, input_data: List[str]
    ) -> Tuple[List[List[str]], List[Tuple[str, int]]]:
        coords = []
        instructions = []

        for line in input_data:
            line = line.strip()
            if "," in line:
                # This is a coordinate pair
                x, y = line.split(",")
                coords.append((int(x), int(y)))
            elif line[0:11] == "fold along ":
                # This is an instruction
                axis, value = line[11:].split("=")
                instructions.append((axis, int(value)))

        return generate_initial_array(coords), instructions

    @classmethod
    def solve_part_1(
        cls, input_data: Tuple[List[List[str]], List[Tuple[str, int]]]
    ) -> int:
        initial, instructions = input_data

        return sum(
            sum([1 for elt in line if elt == "#"])
            for line in fold_sheet(initial, instructions[0])
        )

    @classmethod
    def solve_part_2(cls, input_data: Any) -> None:
        sheet, instructions = input_data
        for instruction in instructions:
            sheet = fold_sheet(sheet, instruction)
        for line in sheet:
            print("".join(line))
