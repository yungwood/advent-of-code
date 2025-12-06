import logging
import os
import sys

import click

from aoc.client import AoCClient
from aoc.cmd.common import day_option, year_option
from aoc.core import PROJECT_ROOT


@click.group(name="client")
@click.option(
    "--token",
    "-t",
    type=str,
    default=None,
    help="Advent of Code session token.",
)
@click.pass_context
def client(ctx, token):
    """Fetch puzzle data automatically"""
    token = os.getenv("AOC_SESSION")
    if not token:
        raise click.UsageError(
            "No session token provided (use --token or set AOC_SESSION)"
        )
    ctx.ensure_object(dict)
    ctx.obj["client"] = AoCClient(token=token)
    pass


@client.command()
@year_option
@day_option
@click.pass_context
def input(ctx, year: int, day: int):
    year_folder = PROJECT_ROOT / f"aoc/{year}"
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        (year_folder / "__init__.py").touch(exist_ok=True)
    input_file = year_folder / f"inputs/day{day:02d}.txt"
    if input_file.exists():
        logging.error(f"Input file %s already exists!", input_file)
        sys.exit(1)
    input = ctx.obj["client"].get_input(year, day)
    input_file.write_text(input.rstrip("\n"))


@client.command()
@year_option
@day_option
@click.pass_context
def fetch(ctx, year: int, day: int):
    year_folder = PROJECT_ROOT / f"aoc/{year}"
    if not year_folder.exists():
        year_folder.mkdir(parents=True, exist_ok=True)
        (year_folder / "__init__.py").touch(exist_ok=True)
    sample_input_file = year_folder / f"inputs/day{day:02d}.sample.txt"
    if sample_input_file.exists():
        logging.error(f"Sample input file %s already exists!", sample_input_file)
        sys.exit(1)
    puzzle = ctx.obj["client"].get_puzzle(day)
    sample_input_file.write_text(puzzle.sample_input)
