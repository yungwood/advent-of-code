import click

from aoc.cmd.common import day_option, year_option
from aoc.cmd.fetch import fetch_puzzle
from aoc.tools.scaffold import create_solution_boilerplate
from aoc.tools.testing import SampleCase, upsert_test_case


@click.group("create")
def cmd_create():
    pass


@cmd_create.command("solution")
@day_option
@year_option
def create_solution(year: int, day: int):
    """Add solution boilerplate for a given day."""
    create_solution_boilerplate(year, day)


@cmd_create.command("test")
@day_option
@year_option
def create_test(year: int, day: int):
    """Add boilerplate for a given day."""
    puzzle = fetch_puzzle(year, day)
    case = SampleCase(year, day, puzzle.answers[0], puzzle.answers[1] or 0)
    upsert_test_case(case)
