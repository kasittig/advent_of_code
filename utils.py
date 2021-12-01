import os
from typing import List


def validate_and_read_file(filepath: str) -> List[str]:
    if not os.path.exists(filepath):
        raise Exception(f"Error: no file found at {filepath}")
    return open(filepath).readlines()


def get_default_input_filename(day: int, year: int) -> str:
    return f"inputs/{year}/day_{day}.txt"
