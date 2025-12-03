from dataclasses import dataclass
from typing import Callable


@dataclass
class Range:
    first: int
    last: int


@dataclass
class ParsedInput:
    ranges: list[Range]


def parse(raw: str) -> ParsedInput:
    puzzle_input = raw.split(",")
    parsed = ParsedInput(ranges=[])
    for item in puzzle_input:
        values = item.split("-")
        parsed.ranges.append(Range(first=int(values[0]), last=int(values[1])))
    return parsed


def part1(data: ParsedInput) -> int:
    invalid = []
    for item in data.ranges:
        invalid.extend(invalid_ids(item.first, item.last, is_invalid_part1))
    return sum(invalid)


def part2(data: ParsedInput) -> int:
    invalid = []
    for item in data.ranges:
        invalid.extend(invalid_ids(item.first, item.last, is_invalid_part2))
    return sum(invalid)


def invalid_ids(start: int, end: int, func: Callable) -> list[int]:
    invalid = []
    for value in range(start, end + 1):
        if func(value):
            invalid.append(value)
    return invalid


def is_invalid_part1(num: int) -> bool:
    value = str(num)
    if len(value) % 2 > 0:
        return False
    j = int(len(value) / 2)
    return value[:j] == value[j:]


def is_invalid_part2(num: int) -> bool:
    value = str(num)
    maxlength = len(value) // 2
    for size in range(1, maxlength + 1):
        if len(value) % size:
            continue
        if all_chunks_equal(value, size):
            return True
    return False


def all_chunks_equal(value: str, size: int):
    first = value[:size]
    for i in range(size, len(value), size):
        if value[i : (i + size)] != first:  # noqa: E203
            return False
    return True
