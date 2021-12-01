from typing import List
from unittest import TestCase

from daily_solutions.year_2020.day_4 import (
    Year2020Day4Solution,
    group_passport_lines,
    is_byr_valid,
    is_ecl_valid,
    is_hcl_valid,
    is_hgt_valid,
    is_pid_valid,
    parse_passport_line,
    passport_is_valid,
)

example: List[str] = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in",
]
passport_1 = (
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
)
passport_2 = "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
passport_3 = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
passport_4 = "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"


class Day4TestCase(TestCase):
    def test_group_passport_lines(self) -> None:
        example_1 = [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
        ]
        self.assertEqual(
            group_passport_lines(example_1),
            [passport_1],
        )

        example_2 = [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
        ]
        self.assertEqual(group_passport_lines(example_2), [passport_1, passport_2])

        self.assertEqual(
            group_passport_lines(example),
            [passport_1, passport_2, passport_3, passport_4],
        )

    def test_parse_passport_line(self) -> None:
        passport_1_result = parse_passport_line(passport_1)
        passport_1_expected = {
            "ecl": "gry",
            "pid": "860033327",
            "eyr": "2020",
            "hcl": "#fffffd",
            "byr": "1937",
            "iyr": "2017",
            "cid": "147",
            "hgt": "183cm",
        }

        self.assertEqual(len(passport_1_expected.keys()), len(passport_1_result.keys()))

        for (k, v) in passport_1_expected.items():
            with self.subTest(k=k):
                self.assertTrue(k in passport_1_result.keys())
                self.assertEqual(passport_1_expected[k], passport_1_result[k])

    def test_passport_is_valid(self) -> None:
        self.assertTrue(passport_is_valid(passport_1))
        self.assertFalse(passport_is_valid(passport_2))
        self.assertTrue(passport_is_valid(passport_3))
        self.assertFalse(passport_is_valid(passport_4))

    def test_count_valid_passports(self) -> None:
        self.assertEqual(
            Year2020Day4Solution().solve_part_1(
                [passport_1, passport_2, passport_3, passport_4]
            ),
            2,
        )

    def test_is_byr_valid(self) -> None:
        self.assertTrue(is_byr_valid("2002"))
        self.assertFalse(is_byr_valid("2003"))

    def test_is_hgt_valid(self) -> None:
        self.assertTrue(is_hgt_valid("60in"))
        self.assertTrue(is_hgt_valid("190cm"))
        self.assertFalse(is_hgt_valid("190in"))
        self.assertFalse(is_hgt_valid("190"))

    def test_is_hcl_valid(self) -> None:
        self.assertTrue(is_hcl_valid("#123abc"))
        self.assertFalse(is_hcl_valid("#123abz"))
        self.assertFalse(is_hcl_valid("123abc"))

    def test_is_ecl_valid(self) -> None:
        self.assertTrue(is_ecl_valid("brn"))
        self.assertFalse(is_ecl_valid("wat"))

    def test_is_pid_valid(self) -> None:
        self.assertTrue(is_pid_valid("000000001"))
        self.assertFalse(is_pid_valid("0123456789"))

    def test_count_valid_passports_with_validation(self) -> None:
        invalid_1 = (
            "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"
        )
        invalid_2 = (
            "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946"
        )
        invalid_3 = "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"
        invalid_4 = (
            "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"
        )
        invalid_passports = [invalid_1, invalid_2, invalid_3, invalid_4]
        for i in range(3):
            with self.subTest(i=i):
                self.assertFalse(passport_is_valid(invalid_passports[i], validate=True))

        valid_1 = (
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f"
        )
        valid_2 = "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"
        valid_3 = "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"
        valid_4 = (
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
        )

        valid_passports = [valid_1, valid_2, valid_3, valid_4]
        for i in range(3):
            with self.subTest(i=i):
                self.assertTrue(passport_is_valid(valid_passports[i], validate=True))
