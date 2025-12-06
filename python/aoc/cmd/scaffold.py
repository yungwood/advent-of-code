import logging
import textwrap

import click

from aoc.cmd.common import day_option, year_option
from aoc.core import PROJECT_ROOT

DAY_TEMPLATE = textwrap.dedent(
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


@click.command()
@day_option
@year_option
def scaffold(year: int, day: int):
    """Add boilerplate for a given DAY."""
    year_folder = PROJECT_ROOT / f"aoc/{year}"
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        (year_folder / "__init__.py").touch(exist_ok=True)
    solution_file = year_folder / f"day{day:02d}.py"
    logging.debug("Adding solution file: %s", solution_file)
    if solution_file.exists():
        logging.error(f"Solutions file %s already exists!", solution_file)
        return
    solution_file.write_text(DAY_TEMPLATE)
