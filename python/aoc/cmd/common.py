from datetime import datetime

import click
import pytz

TARGET_TIMEZONE = pytz.timezone("America/New_York")


def nocache_option(fn):
    return click.option(
        "--no-cache",
        "-f",
        is_flag=True,
        default=False,
        help="Bypass cache and pull from AoC",
    )(fn)


def year_option(fn):
    date = datetime.now(TARGET_TIMEZONE).date()
    default = date.year
    if date.month < 12:
        default = date.year - 1
    return click.option(
        "--year",
        "-y",
        type=click.IntRange(2015, default),
        default=default,
        show_default=True,
    )(fn)


def day_option(fn):
    date = datetime.now(TARGET_TIMEZONE).date()
    default = 1
    if date.month == 12:
        default = min(date.day, 12)
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
