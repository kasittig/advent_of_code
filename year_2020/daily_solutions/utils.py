import os
from typing import List

from year_2020.inputs.config import DAYS_TO_DEFAULT_INPUTS, DEFAULT_INPUT_PATH_PREFIX


def validate_and_read_file(filepath: str) -> List[str]:
    if not os.path.exists(filepath):
        raise Exception(f"Error: no file found at {filepath}")
    return open(filepath).readlines()


def get_default_input_filename(day: int) -> str:
    if day not in DAYS_TO_DEFAULT_INPUTS.keys():
        raise Exception(f"Error: no default input file for day {day}")
    return DEFAULT_INPUT_PATH_PREFIX + DAYS_TO_DEFAULT_INPUTS[day]
