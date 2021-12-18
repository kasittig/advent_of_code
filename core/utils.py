import os
from collections import defaultdict
from typing import Any, Dict, List


def validate_and_read_file(filepath: str) -> List[str]:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error: no file found at {filepath}")
    return open(filepath).readlines()


def get_default_input_filename(day: str, year: str) -> str:
    return f"inputs/{year}/day_{day}.txt"


def get_default_solution_filename(day: str, year: str) -> str:
    return f"daily_solutions/year_{year}/day_{day}.py"


def get_default_test_filename(day: str, year: str) -> str:
    return f"daily_solutions/year_{year}/tests/test_day_{day}.py"


def group_entries_by_line_break(input_lines: List[str]) -> List[List[str]]:
    entries: List[List[str]] = []
    current_entry: List[str] = []

    for line in input_lines:
        line = line.strip()
        if line == "":
            entries.append(current_entry)
            current_entry = []
        else:
            current_entry.append(line.strip())

    if current_entry:
        entries.append(current_entry)
    return entries


def get_frequency_counts(input_list: List[Any]) -> Dict[Any, int]:
    count_dict: Dict[Any, int] = defaultdict(int)
    for elt in input_list:
        count_dict[elt] += 1
    return count_dict
