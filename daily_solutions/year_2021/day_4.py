from typing import Any, Iterable, Tuple

from core.utils import group_entries_by_line_break
from daily_solutions.base import BaseDailySolution

"""
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any
sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the
chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any
row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It
automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For
example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows
(shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case,
the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in
this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the
final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if
you choose that board?

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the
safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it
picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle
column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked
numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""


class BingoBoard(object):
    def __init__(self, rows: list[Iterable[str]]) -> None:
        # Copy the rows to avoid mutating the original board entry list
        self.rows = [[entry for entry in row] for row in rows]

    def mark_entry(self, entry: str) -> bool:
        # Returns a boolean - True if the entry is on this card, False if not
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                if self.rows[i][j] == entry:
                    self.rows[i][j] = "X"
                    return True
        return False

    def _has_winning_row(self) -> bool:
        return any([all([entry == "X" for entry in row]) for row in self.rows])

    def _has_winning_col(self) -> bool:
        return any(
            [
                all([row[i] == "X" for row in self.rows])
                for i in range(len(self.rows[0]))
            ]
        )

    def has_win(self) -> bool:
        return self._has_winning_col() or self._has_winning_row()

    def score(self) -> int:
        return sum([int(entry) for row in self.rows for entry in row if entry != "X"])

    def __repr__(self) -> str:
        return str(self.rows)

    def __eq__(self, other: Any) -> bool:
        if type(other) != BingoBoard:
            return False
        return (
            len(self.rows) == len(other.rows)
            and all(
                len(self.rows[i]) == len(other.rows[i]) for i in range(len(self.rows))
            )
            and all(
                [
                    self.rows[i][j] == other.rows[i][j]
                    for i in range(len(self.rows))
                    for j in range(len(self.rows[i]))
                ]
            )
        )


class Year2021Day4Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 4

    @classmethod
    def format_data(cls, input_data: list[str]) -> Tuple[list[BingoBoard], list[str]]:
        numbers_called = input_data[0].strip().split(",")
        raw_boards = group_entries_by_line_break(input_data[2:])
        boards: list[BingoBoard] = []

        for raw_board in raw_boards:
            raw_rows = [row.split(" ") for row in raw_board]
            clean_rows = [filter(lambda x: x != "", row) for row in raw_rows]
            boards.append(BingoBoard(clean_rows))

        return boards, numbers_called

    @classmethod
    def solve_part_1(cls, input_data: Tuple[list[BingoBoard], list[str]]) -> int:
        boards, numbers_called = input_data

        for number in numbers_called:
            for board in boards:
                board.mark_entry(number)
                if board.has_win():
                    return board.score() * int(number)

        return 0

    @classmethod
    def solve_part_2(cls, input_data: Any) -> Any:
        boards, numbers_called = input_data

        moves_to_win = 0
        score = 0

        for board in boards:
            board_moves = 0
            last_number = 0
            for number in numbers_called:
                board.mark_entry(number)
                board_moves += 1
                if board.has_win():
                    last_number = number
                    break
            if board_moves > moves_to_win:
                moves_to_win = board_moves
                score = board.score() * int(last_number)

        return score
