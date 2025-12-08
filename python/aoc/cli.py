import importlib
import logging
import pkgutil

import click

import aoc.cmd as cmd_pkg

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


def load_commands():
    for module_info in pkgutil.iter_modules(cmd_pkg.__path__):
        module_name = module_info.name
        module = importlib.import_module(f"{cmd_pkg.__name__}.{module_name}")
        function_name = f"cmd_{module_name}"
        if hasattr(module, function_name):
            obj = getattr(module, function_name)
            if isinstance(obj, click.core.Command):
                cli.add_command(obj)


def main():
    load_commands()
    cli(prog_name="aoc")  # pylint: disable=no-value-for-parameter
