from dataclasses import dataclass


@dataclass
class Rotation:
    direction: str
    clicks: int


@dataclass
class ParsedInput:
    rotations: list[Rotation]


def parse(raw: str) -> ParsedInput:
    puzzle_input = raw.splitlines()
    parsed = ParsedInput(rotations=[])
    for line in puzzle_input:
        direction = line[:1]
        clicks = int(line[1:])
        parsed.rotations.append(Rotation(direction=direction, clicks=clicks))
    return parsed


def part1(data: ParsedInput) -> int | str:
    pos = 50
    count = 0
    for rotation in data.rotations:
        clicks = rotation.clicks
        pos = rotate_get_position(
            start=pos, direction=rotation.direction, clicks=clicks
        )
        if pos == 0:
            count += 1
    return count


def part2(data: ParsedInput) -> int | str:
    pos = 50
    count = 0
    for rotation in data.rotations:
        clicks = rotation.clicks
        if clicks >= 100:
            count += clicks // 100
        newpos = rotate_get_position(
            start=pos, direction=rotation.direction, clicks=clicks
        )
        if rotation.direction == "R" and newpos < pos:
            if pos != 0:
                count += 1
        elif rotation.direction == "L" and newpos > pos:
            if pos != 0:
                count += 1
        elif newpos == 0 and clicks > 0:
            count += 1
        pos = newpos
    return count


def rotate_get_position(start: int, direction: str, clicks: int) -> int:
    pos = start
    if clicks > 100:
        clicks = clicks % 100
    if direction == "R":
        pos += clicks
    if direction == "L":
        pos -= clicks
    if pos < 0:
        pos = pos + 100
    if pos >= 100:
        pos = pos - 100
    return pos
