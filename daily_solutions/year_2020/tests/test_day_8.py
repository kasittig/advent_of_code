from unittest import TestCase

from daily_solutions.year_2020.day_8 import ToyHandheldGameConsole

instructions = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]
instruction_tuples = [
    ("nop", 0),
    ("acc", 1),
    ("jmp", 4),
    ("acc", 3),
    ("jmp", -3),
    ("acc", -99),
    ("acc", 1),
    ("jmp", -4),
    ("acc", 6),
]


class Day8SolutionTestCase(TestCase):
    def test_console_step(self) -> None:
        console = ToyHandheldGameConsole()
        for i in range(len(instructions)):
            with self.subTest(i=i):
                self.assertEqual(
                    instruction_tuples[i], console.parse_instruction(instructions[i])
                )
