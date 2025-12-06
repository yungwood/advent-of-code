from dataclasses import dataclass

import pytest

from aoc.core import PROJECT_ROOT, load_day_module, load_input_file


@dataclass(frozen=True)
class SampleCase:
    year: int
    day: int
    expected_part1: int
    expected_part2: int


TESTS = [
    SampleCase(2025, 1, 3, 6),
    SampleCase(2025, 2, 1227775554, 4174379265),
    SampleCase(2025, 3, 357, 3121910778619),
    SampleCase(2025, 4, 13, 43),
    SampleCase(2025, 5, 3, 14),
    SampleCase(2025, 6, 4277556, 3263827),
]


@pytest.mark.parametrize("case", TESTS, ids=[f"{c.year} day {c.day}" for c in TESTS])
def test_day(case: SampleCase):
    data = load_input_file(
        PROJECT_ROOT / f"aoc/{case.year}/inputs/day{case.day:02d}.sample.txt"
    )
    mod = load_day_module(2025, case.day)
    parsed = mod.parse(data)
    assert mod.part1(parsed) == case.expected_part1
    assert mod.part2(parsed) == case.expected_part2
