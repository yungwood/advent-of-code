import sys
from pathlib import Path

import click

from aoc.cmd.common import day_option, nocache_option, part_option, year_option
from aoc.tools.client import AoCClient, AoCPuzzle
from aoc.tools.files import get_input_file, get_sample_input_file


@click.group("fetch")
def cmd_fetch():
    """Fetch puzzle and input data from the Advent of Code site."""


@cmd_fetch.command("puzzle")
@day_option
@year_option
@part_option
@nocache_option
def cmd_puzzle(year: int, day: int, part: int, no_cache: bool):
    """Show puzzle text for a given day and part."""
    puzzle = fetch_puzzle(year, day, no_cache)
    if part == 1:
        print(puzzle.texts[0])
    else:
        if len(puzzle.texts) < 2:
            click.secho("Puzzle part 2 not found!", fg="red")
            sys.exit(1)
        print(puzzle.texts[1])


@cmd_fetch.command("input")
@day_option
@year_option
def cmd_input(year: int, day: int):
    """Fetch puzzle inputs for a given day and part."""
    fetch_sample_input(year, day)
    fetch_puzzle_input(year, day)


def fetch_puzzle(year: int, day: int, no_cache: bool = False) -> AoCPuzzle:
    client = AoCClient()
    return client.get_puzzle(year, day, no_cache)


def fetch_sample_input(year: int, day: int, filepath: Path | None = None) -> bool:
    if filepath is None:
        filepath = get_sample_input_file(year, day)
    if not filepath.exists():
        client = AoCClient()
        puzzle = client.get_puzzle(year, day)
        filepath.write_text(puzzle.sample_input)
        return True
    click.secho(f"Sample input file already exists {filepath}", fg="red")
    return False


def fetch_puzzle_input(year: int, day: int, filepath: Path | None = None) -> bool:
    if filepath is None:
        filepath = get_input_file(year, day)
    if not filepath.exists():
        client = AoCClient()
        puzzle_input = client.get_input(year, day).rstrip("\n")
        filepath.write_text(puzzle_input)
        click.secho(f"Puzzle input saved to {filepath}", fg="green")
        return True
    click.secho(f"Input file already exists {filepath}", fg="red")
    return False
