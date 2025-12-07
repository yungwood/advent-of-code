import sys
from dataclasses import dataclass


@dataclass
class ParsedInput:
    list1: list[int]
    list2: list[int]

    @property
    def length(self):
        return len(self.list1)


def parse(raw: str) -> ParsedInput:
    parsed = ParsedInput([], [])
    for line in raw.splitlines():
        values = line.split()
        parsed.list1.append(int(values[0]))
        parsed.list2.append(int(values[1]))
    return parsed


def part1(data: ParsedInput) -> int:
    data.list1.sort()
    data.list2.sort()
    differences = [abs(a - b) for a, b in zip(data.list1, data.list2)]
    return sum(differences)


def part2(data: ParsedInput) -> int:
    counts = [data.list2.count(i) for i in data.list1]
    scores = [a * b for a, b in zip(counts, data.list1)]
    return sum(scores)


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
