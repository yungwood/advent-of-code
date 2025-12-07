import operator
import sys
from dataclasses import dataclass


@dataclass
class Problem:
    numbers: list[int]

    def solve(self, operation: str) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        result = self.numbers[0]
        for i in self.numbers[1:]:
            result = ops[operation](result, i)

        return result


@dataclass
class ParsedInput:
    operations: list[str]
    lines: list[str]


def parse(raw: str) -> ParsedInput:
    lines = raw.splitlines()
    operations = lines[-1].split()
    return ParsedInput(operations=operations, lines=lines[:-1])


def part1(data: ParsedInput) -> int:
    total = 0
    values = []
    for line in data.lines:
        values.append(i for i in line.split())
    columns = [col for col in zip(*values)]
    for i, column in enumerate(columns):
        total += Problem(numbers=[int(v) for v in column]).solve(data.operations[i])
    return total


def part2(data: ParsedInput) -> int:
    total = 0
    columns = ["".join(col) for col in zip(*data.lines)]
    problems = []
    numbers = []
    for column in columns:
        if column.strip() == "":
            problems.append(Problem(numbers))
            numbers = []
        else:
            numbers.append(int(column))
    problems.append(Problem(numbers))
    for i, problem in enumerate(problems):
        answer = problem.solve(data.operations[i])
        total += answer
    return total


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
