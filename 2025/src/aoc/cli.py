import logging
import sys
import time

import click

from .core import load_day_module, load_input_file

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s [%(module)s.%(funcName)s] %(message)s",
)


@click.group("aoc")
@click.option(
    "--debug",
    "-d",
    is_flag=True,
    default=False,
    help="Output debugging messages to console.",
)
def cli(debug):
    """A cli tool for solving Advent of Code puzzles"""
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Debug logging enabled")


@cli.command()
@click.argument("day", type=int)
@click.option(
    "--part",
    "-p",
    type=click.Choice(["1", "2"]),
    default="1",
    show_default=True,
    help="Which puzzle part to run.",
)
@click.option(
    "--input",
    "-i",
    "filename",
    type=str,
    default=None,
    show_default=True,
    help="Puzzle input file.",
)
def solve(day: int, part: str, filename: str) -> None:
    """Run a given DAY and PART on a given input."""

    if not sys.stdin.isatty():
        stream = click.get_text_stream("stdin")
        raw = stream.read()
    elif filename:
        raw = load_input_file(filename)
    else:
        raise click.UsageError("No input provided (use --input or stdin)")

    start_time = time.time()
    mod = load_day_module(day)
    logging.debug("Parse puzzle input")
    parsed = mod.parse(raw)
    logging.debug("Solve puzzle for day %d part %s", day, part)
    if int(part) == 1:
        result = mod.part1(parsed)
    else:
        result = mod.part2(parsed)
    end_time = time.time()
    elapsed_time = end_time - start_time

    click.secho(result, fg="bright_white", bold=True)
    message = f"Execution took {elapsed_time * 1000:.4f}ms"
    click.secho(message, fg="bright_black", bold=True)


def main():
    cli(prog_name="aoc")  # pylint: disable=no-value-for-parameter
