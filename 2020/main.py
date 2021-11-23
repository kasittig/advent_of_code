from cmd import Cmd
from typing import Iterable
from daily_solutions import DAYS_TO_SOLUTIONS


def is_valid_day(day_str: str) -> bool:
    return day_str.isdecimal() and int(day_str) in DAYS_TO_SOLUTIONS.keys()


class AdventOfCodeCmd(Cmd):
    def do_exit(self, _) -> bool:
        print("Goodbye!")
        return True

    def do_list_days(self, _) -> None:
        print("Days with solutions:")
        days = list(DAYS_TO_SOLUTIONS.keys())
        days.sort()
        for day in days:
            print(f"Day {day}")

    def do_solve(self, args: Iterable[str]) -> None:
        if len(args) == 0:
            print(f"Error: must provide at least one argument (the day to run)!")
            return
        args = args.split()
        day_str = args[0]
        fn_params = args[1:] if len(args) > 1 else []
        if not is_valid_day(day_str):
            print(
                f"Error: no solution implemented for day {day_str}! Use the 'list_days' command to see all solved days."
            )
            return
        day = int(day_str)
        solution_fn = DAYS_TO_SOLUTIONS[day]
        print(f"Running solution script for day {day}")
        try:
            solution_fn(*fn_params)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    AdventOfCodeCmd().cmdloop()
