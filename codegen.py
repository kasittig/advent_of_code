from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())


def generate_daily_template(year: int, day: int) -> None:
    code_template = env.get_template("daily_template.jinja")
    stub = code_template.render(year=year, day=day)
    with open(f"daily_solutions/year_{year}/day_{day}.py", "w") as code_file:
        code_file.write(stub)

    test_template = env.get_template("daily_test_template.jinja")
    test_stub = test_template.render(year=year, day=day)
    with open(f"daily_solutions/year_{year}/tests/test_day_{day}.py", "w") as test_file:
        test_file.write(test_stub)
