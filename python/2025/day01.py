import sys
from dataclasses import dataclass

Rotation = tuple[int, str]
ParsedInput = list[Rotation]


def parse(raw: str) -> ParsedInput:
    puzzle_input = raw.splitlines()
    parsed = ParsedInput([])
    for line in puzzle_input:
        direction = line[:1]
        clicks = int(line[1:])
        parsed.append(Rotation([clicks, direction]))
    return parsed


def part1(data: ParsedInput) -> int | str:
    pos = 50
    count = 0
    for rotation in data:
        pos = rotate_get_position(pos, rotation[0], rotation[1])
        if pos == 0:
            count += 1
    return count


def part2(data: ParsedInput) -> int | str:
    pos = 50
    count = 0
    for clicks, direction in data:
        if clicks >= 100:
            count += clicks // 100
        newpos = rotate_get_position(pos, clicks, direction)
        if direction == "R" and newpos < pos:
            if pos != 0:
                count += 1
        elif direction == "L" and newpos > pos:
            if pos != 0:
                count += 1
        elif newpos == 0 and clicks > 0:
            count += 1
        pos = newpos
    return count


def rotate_get_position(start: int, clicks: int, direction: str) -> int:
    pos = start
    if clicks >= 100:
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


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
