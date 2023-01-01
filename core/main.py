import traceback
from cmd import Cmd
from importlib import reload

import daily_solutions
from core.codegen import generate_daily_template


def is_valid_day(day_str: str, year_str: str = daily_solutions.DEFAULT_YEAR) -> bool:
    return (
        day_str.isdigit()
        and day_str in daily_solutions.SOLUTIONS_BY_YEAR[year_str].keys()
    )


def is_valid_year(year_str: str) -> bool:
    return year_str.isdigit() and year_str in daily_solutions.SOLUTIONS_BY_YEAR.keys()


class AdventOfCodeCmdArgs:
    def __init__(self, day: str, year: str = daily_solutions.DEFAULT_YEAR) -> None:
        self.day = day
        self.year = year

    def is_valid(self) -> bool:
        return is_valid_day(self.day, self.year) and is_valid_year(self.year)


def parse_args(arg_str: str) -> AdventOfCodeCmdArgs:
    args = arg_str.split()
    day_str = args[0]
    year_str = daily_solutions.DEFAULT_YEAR
    if len(args) > 1:
        if len(day_str) == 4:
            year_str = args[0]
            day_str = args[1]
        else:
            year_str = args[1]
    return AdventOfCodeCmdArgs(day_str, year_str)


class AdventOfCodeCmd(Cmd):
    @staticmethod
    def do_exit(_) -> bool:
        print("Goodbye!")
        return True

    @staticmethod
    def do_list_days(_) -> None:
        print("Days with solutions, by year:")
        for year in daily_solutions.SOLUTIONS_BY_YEAR.keys():
            print(f"{year}")
            days = list(daily_solutions.SOLUTIONS_BY_YEAR[year].keys())
            days.sort()
            if len(days) == 0:
                print("  (None yet!)")
                print(" ")
                continue
            for day in days:
                print(f"* Day {day}")
            print(" ")

    @staticmethod
    def do_solve(args: str) -> None:
        if len(args) == 0:
            print("Error: must provide at least one argument (the day to run)!")
            return
        args = parse_args(args)
        if not args.is_valid():
            print(
                f"Error: no solution implemented for {args.year} day {args.day}! Use "
                "the 'list_days' command to see all solved days by year."
            )
            return
        solution_class = daily_solutions.SOLUTIONS_BY_YEAR[args.year][args.day]
        print(f"Running solution script for {args.year} day {args.day}")
        try:
            solution_class().solve()
        except Exception:
            print(traceback.format_exc())

    @staticmethod
    def do_setup(args: str) -> None:
        if len(args) == 0:
            print("Error: must provide at least one argument (the day to run)!")
            return
        args = parse_args(args)
        if args.is_valid():
            print(
                f"Error: solution file already exists for {args.year} day "
                f"{args.day}! Use the 'list_days' command to see all solved "
                "days by year."
            )
            return
        print(
            f"Generating template solution file and tests for {args.year} day "
            f"{args.day}"
        )
        try:
            generate_daily_template(args.day, args.year)

            # Reload all the daily solutions in order to access our new solution
            reload(daily_solutions.year_2020)
            reload(daily_solutions.year_2021)
            reload(daily_solutions)
        except Exception:
            print(traceback.format_exc())


if __name__ == "__main__":
    AdventOfCodeCmd().cmdloop()
