from unittest import TestCase

from daily_solutions.year_2021.day_11 import OctopusGrid, Year2021Day11Solution

initial = [
    [1, 1, 1, 1, 1],
    [1, 9, 9, 9, 1],
    [1, 9, 1, 9, 1],
    [1, 9, 9, 9, 1],
    [1, 1, 1, 1, 1],
]

step_1 = [
    [3, 4, 5, 4, 3],
    [4, 0, 0, 0, 4],
    [5, 0, 0, 0, 5],
    [4, 0, 0, 0, 4],
    [3, 4, 5, 4, 3],
]

example = [
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
]


class Day11SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day11Solution

    def test_solve_part_1(self) -> None:
        self.assertEqual(1656, self.solution.solve_part_1(example))

    def test_solve_part_2(self) -> None:
        self.assertEqual(195, self.solution.solve_part_2(example))


class OctopusGridTestCase(TestCase):
    def setUp(self) -> None:
        self.octopus_grid_small = OctopusGrid(initial)
        self.octopus_grid_large = OctopusGrid(example)

    def test_step(self) -> None:
        self.assertEqual(initial, self.octopus_grid_small.data_grid)
        self.octopus_grid_small.do_step()
        self.assertEqual(step_1, self.octopus_grid_small.data_grid)
        self.assertEqual(9, self.octopus_grid_small.total_flashes)

        self.octopus_grid_large.do_step()
        self.assertEqual(0, self.octopus_grid_large.total_flashes)
        self.octopus_grid_large.do_step()
        self.assertEqual(35, self.octopus_grid_large.total_flashes)
