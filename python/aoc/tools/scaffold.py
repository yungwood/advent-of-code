import textwrap

import click

from aoc.tools.files import get_year_folder

SOLUTION_TEMPLATE = textwrap.dedent(
    """    import sys
    from dataclasses import dataclass


    @dataclass
    class ParsedInput:
        raw: list[str]


    def parse(raw: str) -> ParsedInput:
        lines = raw.splitlines()
        return ParsedInput(lines)


    def part1(data: ParsedInput) -> int:
        return 0


    def part2(data: ParsedInput) -> int:
        return 0


    if __name__ == "__main__":
        raw = sys.stdin.read()
        if not raw:
            print("No input received on stdin.")
            sys.exit(1)

        data = parse(raw)
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
"""
)


def create_solution_boilerplate(year: int, day: int) -> None:
    year_folder = get_year_folder(year)
    solution_file = year_folder / f"day{day:02d}.py"
    if not solution_file.exists():
        click.secho(f"Creating solution file {solution_file}", fg="blue")
        solution_file.write_text(SOLUTION_TEMPLATE)
    else:
        click.secho(f"Solution file already exists {solution_file}", fg="red")
