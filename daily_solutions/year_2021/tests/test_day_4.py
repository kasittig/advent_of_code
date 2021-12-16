from unittest import TestCase

from daily_solutions.year_2021.day_4 import BingoBoard, Year2021Day4Solution

board_1_parsed = [
    ["22", "13", "17", "11", "0"],
    ["8", "2", "23", "4", "24"],
    ["21", "9", "14", "16", "7"],
    ["6", "10", "3", "18", "5"],
    ["1", "12", "20", "15", "19"],
]


class BingoBoardTestCase(TestCase):
    def setUp(self) -> None:
        self.board = BingoBoard(board_1_parsed)

    def test_init(self) -> None:
        self.assertIsNotNone(self.board.rows)
        for i in range(len(self.board.rows)):
            with self.subTest(i=i):
                self.assertEqual(self.board.rows[i], board_1_parsed[i])

    def test_mark_entry(self) -> None:
        self.assertTrue(self.board.mark_entry("1"))
        self.assertTrue(self.board.rows[4][0] == "X")

        self.assertFalse(self.board.mark_entry("77"))

    def test_has_winning_row(self) -> None:
        for entry in ["1", "12", "20", "15"]:
            with self.subTest(entry=entry):
                self.board.mark_entry(entry)
                self.assertFalse(self.board._has_winning_row())
        self.board.mark_entry("19")
        self.assertTrue(self.board._has_winning_row())

    def test_has_winning_col(self) -> None:
        for entry in ["8", "21", "6", "22"]:
            with self.subTest(entry=entry):
                self.board.mark_entry(entry)
                self.assertFalse(self.board._has_winning_col())
        self.board.mark_entry("1")
        self.assertTrue(self.board._has_winning_col())

    def test_has_win(self) -> None:
        self.assertFalse(self.board.has_win())
        for entry in ["1", "8", "21", "6"]:
            self.board.mark_entry(entry)
            self.assertFalse(self.board.has_win())

        # Mark one more entry not in this column
        self.board.mark_entry("19")
        self.assertFalse(self.board.has_win())

        # For the win!
        self.board.mark_entry("22")
        self.assertTrue(self.board.has_win())

    def test_score_board(self) -> None:
        self.assertEqual(self.board.score(), 300)

        self.board.mark_entry("22")
        self.assertEqual(self.board.score(), 278)

        self.board.mark_entry("22")
        self.assertEqual(self.board.score(), 278)

        self.board.mark_entry("1")
        self.assertEqual(self.board.score(), 277)


example_file = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
]


class Day4TestCase(TestCase):
    def setUp(self) -> None:
        self.tc = Year2021Day4Solution()

    def test_format_data(self) -> None:
        boards, numbers_called = self.tc.format_data(example_file)

        self.assertEqual(len(boards), 3)
        self.assertEqual(boards[0], BingoBoard(board_1_parsed))
        self.assertEqual(
            numbers_called,
            [
                "7",
                "4",
                "9",
                "5",
                "11",
                "17",
                "23",
                "2",
                "0",
                "14",
                "21",
                "24",
                "10",
                "16",
                "13",
                "6",
                "15",
                "25",
                "12",
                "22",
                "18",
                "20",
                "8",
                "19",
                "3",
                "26",
                "1",
            ],
        )

    def test_solve_part_1(self) -> None:
        input_data = self.tc.format_data(example_file)
        self.assertEqual(self.tc.solve_part_1(input_data), 4512)

    def test_solve_part_2(self) -> None:
        input_data = self.tc.format_data(example_file)
        self.assertEqual(1924, self.tc.solve_part_2(input_data))
