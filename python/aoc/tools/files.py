"""
Common functions
"""

import importlib
import logging
import sys
from pathlib import Path

import click

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_text_file(filename) -> str:
    path = Path(filename)
    logging.debug("Reading input from file: %s", filename)
    if not path.exists():
        logging.error("Input file not found: %s", path)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def get_year_folder(year: int) -> Path:
    year_folder = PROJECT_ROOT / f"{year}"
    if not year_folder.exists():
        click.secho(f"Creating folder {year_folder}", fg="bright_black")
        year_folder.mkdir()
    year_init = year_folder / "__init__.py"
    if not year_init.exists():
        click.secho(f"Creating file {year_init}", fg="bright_black")
        year_init.touch()
    return year_folder


def get_inputs_folder(year: int) -> Path:
    inputs_folder = get_year_folder(year) / "inputs"
    if not inputs_folder.exists():
        click.secho(f"Creating folder {inputs_folder}", fg="bright_black")
        inputs_folder.mkdir()
    return inputs_folder


def get_input_file(year: int, day: int) -> Path:
    return get_inputs_folder(year) / f"day{day:02d}.txt"


def get_sample_input_file(year: int, day: int) -> Path:
    return get_inputs_folder(year) / f"day{day:02d}.sample.txt"


def get_cache_folder() -> Path:
    cache_folder = PROJECT_ROOT / ".cache"
    if not cache_folder.exists():
        click.secho(f"Creating folder {cache_folder}", fg="bright_black")
        cache_folder.mkdir()
    return cache_folder
