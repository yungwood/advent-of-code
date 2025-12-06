import logging
import sys
import time

import click

from aoc.cmd.common import day_option, part_option, year_option
from aoc.core import PROJECT_ROOT, load_day_module, load_input_file


@click.command("solve")
@year_option
@day_option
@part_option
@click.option(
    "--input",
    "-i",
    "filename",
    type=str,
    default=None,
    help="Puzzle input file.",
)
def solve(year: int, day: int, part: str, filename: str) -> None:
    """Run a given DAY and PART on a given input."""
    click.secho(f"Solving {year} day {day} part {part}", fg="blue")
    if not sys.stdin.isatty():
        logging.debug("Reading input from stdin")
        stream = click.get_text_stream("stdin")
        raw = stream.read()
    elif filename:
        raw = load_input_file(filename)
    else:
        raw = load_input_file(PROJECT_ROOT / f"inputs/{year}/day{day:02d}.sample.txt")
    start_time = time.time()
    mod = load_day_module(year, day)
    logging.debug(f"Parse puzzle input for {year} day {day}")
    parsed = mod.parse(raw)
    logging.debug(f"Solve puzzle for {year} day {day} part {part}")
    if int(part) == 1:
        result = mod.part1(parsed)
    else:
        result = mod.part2(parsed)
    end_time = time.time()
    elapsed_time = end_time - start_time

    click.echo("The answer is: " + click.style(result, fg="bright_white", bold=True))
    message = f"Execution took {elapsed_time * 1000:.4f}ms"
    click.secho(message, fg="bright_black")
