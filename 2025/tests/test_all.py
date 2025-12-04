import pytest

from dataclasses import dataclass
from typing import Optional

from aoc.core import load_day_module, load_input_file


@dataclass(frozen=True)
class SampleCase:
    day: int
    expected_part1: Optional[int | str] = None
    expected_part2: Optional[int | str] = None


TESTS = [
    SampleCase(day=1, expected_part1=3, expected_part2=6),
    SampleCase(
        day=2,
        expected_part1=1227775554,
        expected_part2=4174379265,
    ),
    SampleCase(
        day=3,
        expected_part1=357,
        expected_part2=3121910778619,
    ),
    SampleCase(
        day=4,
        expected_part1=13,
        expected_part2=43,
    ),
]


@pytest.mark.parametrize("case", TESTS, ids=[c.day for c in TESTS])
def test_day(case: SampleCase):
    data = load_input_file(
        f"inputs/day{case.day:02d}.sample.txt",
    )
    mod = load_day_module(case.day)
    parsed = mod.parse(data)
    if case.expected_part1 is not None:
        assert mod.part1(parsed) == case.expected_part1
    if case.expected_part2 is not None:
        assert mod.part2(parsed) == case.expected_part2
