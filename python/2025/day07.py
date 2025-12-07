import sys
from dataclasses import dataclass


@dataclass
class ParsedInput:
    grid: list[str]


def parse(raw: str) -> ParsedInput:
    return ParsedInput(grid=raw.splitlines())


def part1(data: ParsedInput) -> int:
    splits = 0
    tachyons = {data.grid[0].find("S")}

    for row in data.grid[1:]:
        new_tachyons = set(tachyons)
        for i in tachyons:
            if row[i] == "^":
                splits += 1
                new_tachyons.discard(i)
                new_tachyons.add(i - 1)
                new_tachyons.add(i + 1)
        tachyons = new_tachyons
    return splits


def part2(data: ParsedInput) -> int:
    start_tachyon = data.grid[0].find("S")
    cache: dict[tuple[int, int], int] = {}

    def count_paths(tachyon: int, index: int) -> int:
        key = (tachyon, index)
        if key in cache:
            return cache[key]

        if index == len(data.grid) - 1:
            cache[key] = 1
            return 1

        if data.grid[index][tachyon] == "^":
            value = count_paths(tachyon - 1, index + 1)
            value += count_paths(tachyon + 1, index + 1)
        else:
            value = count_paths(tachyon, index + 1)

        cache[key] = value
        return value

    return count_paths(start_tachyon, 0)


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
