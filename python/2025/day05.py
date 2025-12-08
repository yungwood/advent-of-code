import sys
from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def contains(self, value: int) -> bool:
        return self.start <= value <= self.end

    def size(self) -> int:
        return self.end - self.start + 1


@dataclass
class ParsedInput:
    ranges: list[Range]
    values: list[int]


def parse(raw: str) -> ParsedInput:
    inputs = raw.split("\n\n")
    ranges: list[Range] = []
    for item in inputs[0].splitlines():
        values = item.split("-")
        ranges.append(Range(start=int(values[0]), end=int(values[1])))
    values = [int(i) for i in inputs[1].splitlines()]
    return ParsedInput(ranges=ranges, values=values)


def part1(data: ParsedInput) -> int:
    ranges = dedupe_ranges(data.ranges)
    good = 0
    for value in data.values:
        if any(r.contains(value) for r in ranges):
            good += 1
    return good


def part2(data: ParsedInput) -> int:
    ranges = dedupe_ranges(data.ranges)
    return sum(r.size() for r in ranges)


def dedupe_ranges(ranges: list[Range]):
    deduped = []
    ranges = sorted(ranges, key=lambda x: x.start)
    for r in ranges:
        if not deduped or not deduped[-1].contains(r.start):
            deduped.append(r)
        else:
            last = deduped[-1]
            last.end = max([last.end, r.end])
    return deduped


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
