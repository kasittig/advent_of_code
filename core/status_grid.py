from typing import Any, Callable


class BaseStatusGrid(object):
    DEFAULT_STATUS = None

    def __init__(self, initial_data: list[list[Any]]) -> None:
        self.data_grid = initial_data
        self.max_height = len(self.data_grid)
        self.max_width = len(self.data_grid[0])
        self.status_grid = [
            [self.DEFAULT_STATUS for _ in range(self.max_width)]
            for _ in range(self.max_height)
        ]

    def do_for_each(self, fn: Callable) -> None:
        for i in range(self.max_height):
            for j in range(self.max_width):
                fn(i, j)

    def is_out_of_bounds(self, i: int, j: int) -> bool:
        return i < 0 or i >= self.max_height or j < 0 or j >= self.max_width

    def reset_status(self) -> None:
        self.status_grid = [
            [self.DEFAULT_STATUS for _ in range(self.max_width)]
            for _ in range(self.max_height)
        ]
