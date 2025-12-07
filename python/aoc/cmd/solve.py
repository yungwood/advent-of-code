import importlib
import logging
import sys
import time

import click

from aoc.cmd.common import day_option, part_option, year_option
from aoc.tools.files import get_input_file, get_sample_input_file, load_text_file


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
@click.option(
    "--real-input",
    "-r",
    is_flag=True,
    default=False,
    help="Default to real puzzle input file.",
)
def solve(year: int, day: int, part: str, filename: str, real_input: bool) -> None:
    """Run a given YEAR, DAY and PART on a given or saved input."""
    if not sys.stdin.isatty():
        logging.debug("Reading input from stdin")
        stream = click.get_text_stream("stdin")
        raw = stream.read()
    elif filename:
        raw = load_text_file(filename)
    elif real_input:
        raw = load_text_file(get_input_file(year, day))
    else:
        raw = load_text_file(get_sample_input_file(year, day))
    click.secho(f"Solution for AoC {year} day {day} part {part}", fg="blue")
    start_time = time.time()
    try:
        mod = importlib.import_module(f"{year}.day{day:02d}")
    except ModuleNotFoundError:
        click.secho(f"Module not found at {year}/day{day:02d}.py", fg="red")
        sys.exit(1)
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
