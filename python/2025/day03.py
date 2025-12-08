import sys

Bank = list[int]
ParsedInput = list[Bank]


def parse(raw: str) -> ParsedInput:
    parsed = ParsedInput([])
    puzzle_input = raw.splitlines()
    for bank in puzzle_input:
        parsed.append(Bank([int(i) for i in bank]))
    return parsed


def part1(data: ParsedInput) -> int:
    max_joltage = 0
    for bank in data:
        max_joltage += find_max_joltage(bank, 2)
    return max_joltage


def part2(data: ParsedInput) -> int:
    max_joltage = 0
    for bank in data:
        max_joltage += find_max_joltage(bank, 12)
    return max_joltage


def find_max_joltage(bank: Bank, battery_count: int) -> int:
    joltages = []
    for i in range(battery_count - 1, -1, -1):
        if i == 0:
            haystack = bank
        else:
            haystack = bank[:-i]
        joltages.append(max(haystack))
        pos = bank.index(joltages[-1])
        bank = bank[pos + 1 :]
    max_joltage = "".join([str(i) for i in joltages])
    return int(max_joltage)


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
