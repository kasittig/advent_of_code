from typing import List, Tuple, Optional
from daily_solutions.utils import validate_and_read_file, get_default_input_filename

"""
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of
a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579,
so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply
them together?

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from
a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same
criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""


def target_in_list(target: int, number_list: List[int]) -> bool:
    for elt in number_list:
        if elt == target:
            return True
    return False


def get_target_number_pair(number_list: List[int], target_sum: int = 2020) -> Tuple[Optional[int], Optional[int]]:
    for i in range(len(number_list)):
        target_val = target_sum - number_list[i]
        if target_in_list(target_val, number_list[i+1:]):
            return number_list[i], target_val
    return None, None


def solve_part_1(number_list: List[int], target_sum: int = 2020) -> Tuple[Optional[int], Optional[int]]:
    return get_target_number_pair(number_list, target_sum)


def solve_part_2(number_list: List[int], target_sum: int = 2020) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    for i in range(len(number_list) - 1):
        val1 = number_list[i]
        val2, val3 = get_target_number_pair(number_list[i+1:], target_sum - val1)
        if val2 is not None and val3 is not None:
            return val1, val2, val3
    return None, None, None


def solve_day_1(filename: Optional[str] = None, target_sum: int = 2020) -> None:
    if not filename:
        filename = get_default_input_filename(1)
    number_list = list(map(int, validate_and_read_file(filename)))

    # Solve part 1
    val1, val2 = solve_part_1(number_list, target_sum)
    if val1 is None or val2 is None:
        print(f"Couldn't find two integers that sum to {target_sum} in input list")
    else:
        print(f"Found {val1} and {val2} which multiply to {val1 * val2}")

    # Solve part 2
    val1, val2, val3 = solve_part_2(number_list, target_sum)
    if val1 is None or val2 is None or val3 is None:
        print(f"Couldn't find three integers that sum to {target_sum} in input list")
    else:
        print(f"Found {val1}, {val2}, and {val3} which multiply to {val1 * val2 * val3}")