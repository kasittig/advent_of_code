from typing import List

from utils import get_default_input_filename, validate_and_read_file


def get_input_filename(day: int) -> str:
    return get_default_input_filename(day, 2021)


def get_input_file(day: int) -> List[str]:
    filename = get_input_filename(day)
    return validate_and_read_file(filename)
