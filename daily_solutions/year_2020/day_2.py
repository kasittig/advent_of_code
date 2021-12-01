import re
from typing import Tuple

from daily_solutions.year_2020.utils import get_input_file

"""
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we
can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official
Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted
database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number
of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but
needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of
their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the
sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""


def parse_string_entry(entry: str) -> Tuple[int, int, str, str]:
    regex_pattern = r"(\d+)\-(\d+) (\w): (\w+)"
    m = re.match(regex_pattern, entry).groups()
    if len(m) == 4:
        return int(m[0]), int(m[1]), m[2], m[3]
    else:
        raise Exception(f"Input line {entry} is incorrectly formatted!")


def is_valid_password_part_1(
    min_count: int, max_count: int, target_letter: str, password: str
) -> bool:
    letter_count = 0
    for letter in password:
        if letter == target_letter:
            letter_count += 1
    return min_count <= letter_count <= max_count


def is_valid_password_part_2(
    index1: int, index2: int, target_letter: str, password: str
) -> bool:
    return (password[index1 - 1] == target_letter) != (
        password[index2 - 1] == target_letter
    )


def solve_day_2() -> None:
    password_entries = get_input_file(2)
    count_part_1 = 0
    count_part_2 = 0

    for entry in password_entries:
        int1, int2, target_letter, password = parse_string_entry(entry)
        count_part_1 += (
            1 if is_valid_password_part_1(int1, int2, target_letter, password) else 0
        )
        count_part_2 += (
            1 if is_valid_password_part_2(int1, int2, target_letter, password) else 0
        )
    print(f"Found {count_part_1} valid passwords for part 1")
    print(f"Found {count_part_2} valid passwords for part 2")
