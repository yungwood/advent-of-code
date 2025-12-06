"""
Common functions
"""

import importlib
import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_day_module(day: int):
    day_str = f"day{day:02d}"
    logging.debug("Loading module aoc.days.%s", day_str)
    return importlib.import_module(f"aoc.days.{day_str}")


def load_input_file(filename) -> str:
    path = Path(filename)
    logging.debug("Reading input from file: %s", filename)
    if not path.exists():
        logging.error("Input file not found: %s", path)
        sys.exit(1)
    return path.read_text(encoding="utf-8")
