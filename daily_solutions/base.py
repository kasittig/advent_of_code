from abc import ABC, abstractmethod
from typing import Any, List

from utils import get_default_input_filename, validate_and_read_file


class BaseDailySolution(ABC):
    YEAR = NotImplemented
    DAY = NotImplemented

    @classmethod
    def get_input_data(cls) -> List[str]:
        filename = get_default_input_filename(cls.DAY, cls.YEAR)
        return validate_and_read_file(filename)

    @classmethod
    def format_data(cls, input_data: List[str]) -> Any:
        return input_data

    @classmethod
    def solve(cls) -> None:
        data = cls.format_data(cls.get_input_data())
        part_1 = cls.solve_part_1(data)
        print(f"Part 1 solution: {part_1}")
        part_2 = cls.solve_part_2(data)
        print(f"Part 2 solution: {part_2}")

    @classmethod
    @abstractmethod
    def solve_part_1(cls, input_data: Any) -> Any:
        pass

    @classmethod
    @abstractmethod
    def solve_part_2(cls, input_data: Any) -> Any:
        pass
