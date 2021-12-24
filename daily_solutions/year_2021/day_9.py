from collections import defaultdict
from typing import List, Tuple

from core.status_grid import BaseStatusGrid
from daily_solutions.base import BaseDailySolution

"""
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into
the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The
submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location
can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most
locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have
three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the
third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent
location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6,
and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin,
although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations
will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four
basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""


class HeightMap(BaseStatusGrid):
    DEFAULT_STATUS = "*"

    def count_adjacent_less_than(self, i: int, j: int) -> int:
        value = self.data_grid[i][j]

        return sum(
            [
                int(self.get_value(i - 1, j) >= value),
                int(self.get_value(i + 1, j) >= value),
                int(self.get_value(i, j - 1) >= value),
                int(self.get_value(i, j + 1) >= value),
            ]
        )

    def get_all_low_points(self) -> List[Tuple[int, int]]:
        low_points: List[Tuple[int, int]] = []
        for i in range(self.max_height):
            for j in range(self.max_width):
                if self.count_adjacent_less_than(i, j) == 4:
                    low_points.append((i, j))
        return low_points

    def get_value(self, i: int, j: int) -> int:
        if self.is_out_of_bounds(i, j):
            return 10
        else:
            return self.data_grid[i][j]

    def generate_basin_map(self) -> None:
        # Initialize low points on basin map
        low_points = self.get_all_low_points()
        basin_no = 0
        for low_point in low_points:
            i, j = low_point
            self.status_grid[i][j] = basin_no
            basin_no += 1

        # Mark all of the 9s
        for i in range(self.max_height):
            for j in range(self.max_width):
                if self.data_grid[i][j] == 9:
                    self.status_grid[i][j] = "X"

        done = self._do_basin_step()

        while not done:
            done = self._do_basin_step()

    def _do_basin_step(self) -> bool:
        done = True
        # For each point, try to add it to the adjacent basin
        for i in range(self.max_height):
            for j in range(self.max_width):
                if self.status_grid[i][j] != "*":
                    # This point has already been put in a basin
                    continue

                done = False
                value = self.data_grid[i][j]
                # Check and mark the adjacent points
                for (ii, jj) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if self.is_out_of_bounds(ii, jj):
                        continue
                    if self.data_grid[ii][jj] < value:
                        adjacent_basin = self.status_grid[ii][jj]
                        if adjacent_basin not in ["X", "*"]:
                            self.status_grid[i][j] = adjacent_basin
                            break
        return done

    def count_basin_sizes(self) -> List[int]:
        basin_sizes = defaultdict(int)
        for i in range(self.max_height):
            for j in range(self.max_width):
                basin_sizes[self.status_grid[i][j]] += 1

        return [v for (k, v) in basin_sizes.items() if k != "X"]


class Year2021Day9Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 9

    @classmethod
    def format_data(cls, input_data: List[str]) -> List[List[int]]:
        return [[int(c) for c in line.strip()] for line in input_data]

    @classmethod
    def solve_part_1(cls, input_data: List[List[int]]) -> int:
        heightmap = HeightMap(input_data)
        low_points = heightmap.get_all_low_points()

        return sum(input_data[i][j] + 1 for (i, j) in low_points)

    @classmethod
    def solve_part_2(cls, input_data: List[List[int]]) -> int:
        heightmap = HeightMap(input_data)
        heightmap.generate_basin_map()
        basins = heightmap.count_basin_sizes()
        basins.sort(reverse=True)
        return basins[0] * basins[1] * basins[2]
