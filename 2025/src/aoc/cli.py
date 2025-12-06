import logging

import click

from aoc.cmd.client import client
from aoc.cmd.scaffold import scaffold
from aoc.cmd.solve import solve

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


cli.add_command(client)
cli.add_command(scaffold)
cli.add_command(solve)


def main():
    click.secho("Advent of Code", fg="green", bold=True)
    cli(prog_name="aoc")  # pylint: disable=no-value-for-parameter
