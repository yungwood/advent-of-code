from datetime import date

import click


def day_option(fn):
    default = 1
    if date.today().month == 12:
        default = min(date.today().day, 12)
    return click.option(
        "--day",
        "-d",
        type=click.IntRange(1, 12),
        default=default,
        show_default=True,
    )(fn)


def part_option(fn):
    return click.option(
        "--part",
        "-p",
        type=click.Choice(["1", "2"]),
        default="1",
        show_default=True,
        help="Which puzzle part to run.",
    )(fn)
