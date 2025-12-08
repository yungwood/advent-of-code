import operator
import sys
from dataclasses import dataclass

Problem = list[int]


@dataclass
class ParsedInput:
    lines: list[str]
    operations: list[str]


def parse(raw: str) -> ParsedInput:
    lines = raw.splitlines()
    operations = lines[-1].split()
    return ParsedInput(lines[:-1], operations)


def part1(data: ParsedInput) -> int:
    total = 0
    problems = lines_to_problems_part1(data.lines)
    for problem, op in zip(problems, data.operations):
        total += solve(problem, op)
    return total


def part2(data: ParsedInput) -> int:
    total = 0
    problems = lines_to_problems_part2(data.lines)
    for problem, op in zip(problems, data.operations):
        answer = solve(problem, op)
        total += answer
    return total


def lines_to_problems_part1(lines: list[str]) -> list[Problem]:
    values = []
    for line in lines:
        values.append([int(i) for i in line.split()])
    return [Problem(col) for col in zip(*values)]


def lines_to_problems_part2(lines: list[str]) -> list[Problem]:
    columns = ["".join(col) for col in zip(*lines)]
    problems = []
    numbers = []
    for column in columns:
        if column.strip() == "":
            problems.append(Problem(numbers))
            numbers = []
        else:
            numbers.append(int(column))
    problems.append(Problem(numbers))
    return problems


def solve(problem: Problem, operation: str) -> int:
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result = problem[0]
    for i in problem[1:]:
        result = ops[operation](result, i)

    return result


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
