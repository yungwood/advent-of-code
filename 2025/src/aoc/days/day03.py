from dataclasses import dataclass


@dataclass
class Bank:
    batteries: list[int]


@dataclass
class ParsedInput:
    banks: list[Bank]


def parse(raw: str) -> ParsedInput:
    parsed = ParsedInput(banks=[])
    puzzle_input = raw.splitlines()
    for bank in puzzle_input:
        parsed.banks.append(Bank([int(i) for i in bank]))
    return parsed


def part1(data: ParsedInput) -> int:
    max_joltage = 0
    for bank in data.banks:
        max_joltage += find_max_joltage(bank.batteries, 2, [])
    return max_joltage


def part2(data: ParsedInput) -> int:
    max_joltage = 0
    for bank in data.banks:
        max_joltage += find_max_joltage(bank.batteries, 12, [])
    return max_joltage


def find_max_joltage(bank: list[int], max_active: int, joltages: list[int]) -> int:
    for i in range(9, -1, -1):
        try:
            index = bank.index(i)
        except ValueError:
            continue

        if index > len(bank) - max_active + len(joltages):
            continue

        joltages.append(i)

        if max_active == len(joltages):
            max_joltage = "".join([str(i) for i in joltages])
            return int(max_joltage)

        return find_max_joltage(bank[index + 1 :], max_active, joltages)  # noqa: E203

    raise LookupError("Finished walking tree with no result!")
