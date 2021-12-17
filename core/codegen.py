import os
from typing import List

from jinja2 import Environment, FileSystemLoader, select_autoescape

from core.utils import get_default_solution_filename, get_default_test_filename

env = Environment(
    loader=FileSystemLoader("core/templates"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)


def generate_daily_template(day: str, year: str) -> None:
    code_template = env.get_template("daily_template.jinja")
    stub = code_template.render(year=year, day=day)
    with open(get_default_solution_filename(day, year), "w") as code_file:
        code_file.write(stub)

    test_template = env.get_template("daily_test_template.jinja")
    test_stub = test_template.render(year=year, day=day)
    with open(get_default_test_filename(day, year), "w") as test_file:
        test_file.write(test_stub)

    generate_imports(year)


def generate_imports(year: str) -> None:
    import_template = env.get_template("init_file.jinja")
    days = get_days(year)
    import_contents = import_template.render(days=days, year=year)
    with open(f"daily_solutions/year_{year}/__init__.py", "w") as import_file:
        import_file.write(import_contents)


def get_days(year: str) -> List[str]:
    days: List[str] = []
    for i in range(1, 32):
        if os.path.exists(get_default_solution_filename(str(i), year)):
            days.append(str(i))
    return days
