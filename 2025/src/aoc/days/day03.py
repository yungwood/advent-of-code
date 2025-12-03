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
        max_joltage += find_max_joltage(bank.batteries, 2)
    return max_joltage


def part2(data: ParsedInput) -> int:
    max_joltage = 0
    for bank in data.banks:
        max_joltage += find_max_joltage(bank.batteries, 12)
    return max_joltage


def find_max_joltage(bank: list[int], battery_count: int) -> int:
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
