import logging
import re
import textwrap

import click

from aoc.tools.files import get_tests_file, get_year_folder

SAMPLE_RE = re.compile(r"SampleCase\(([^)]*)\)")
SOLUTION_TEMPLATE = textwrap.dedent(
    """    import sys
    from dataclasses import dataclass


    @dataclass
    class ParsedInput:
        raw: list[str]


    def parse(raw: str) -> ParsedInput:
        lines = raw.splitlines()
        return ParsedInput(lines)


    def part1(data: ParsedInput) -> int:
        return 0


    def part2(data: ParsedInput) -> int:
        return 0


    if __name__ == "__main__":
        raw = sys.stdin.read()
        if not raw:
            print("No input received on stdin.")
            sys.exit(1)

        data = parse(raw)
        print("Part 1:", part1(data))
        print("Part 2:", part2(data))
"""
)


def parse_tests_block(lines: list[str]) -> dict[int, tuple[str, str]]:
    """
    Parse TESTS list into {day: (p1_code, p2_code)}.
    Values are kept as raw code strings.
    """
    tests: dict[int, tuple[str, str]] = {}

    for line in lines:
        m = SAMPLE_RE.search(line)
        if not m:
            continue
        args = [a.strip() for a in m.group(1).split(",") if a.strip()]
        if not args:
            continue
        day = int(args[0])
        p1 = args[1] if len(args) > 1 else "None"
        p2 = args[2] if len(args) > 2 else "None"
        tests[day] = (p1, p2)

    return tests


def render_tests_block(tests: dict[int, tuple[str, str]]) -> list[str]:
    """
    Render the TESTS block from {day: (p1_code, p2_code)}.
    """
    lines: list[str] = []
    lines.append("TESTS = [")
    for day in sorted(tests):
        p1, p2 = tests[day]
        lines.append(f"    SampleCase({day}, {p1}, {p2}),")
    lines.append("]")
    return lines


def upsert_sample_case(day: int, p1: int, p2: int) -> None:
    test_file = get_tests_file()
    text = test_file.read_text()
    lines = text.splitlines()

    start_idx = end_idx = None

    # Locate TESTS block
    for i, line in enumerate(lines):
        if start_idx is None and line.strip().startswith("TESTS = ["):
            start_idx = i
            continue
        if start_idx is not None and line.strip().startswith("]"):
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        raise RuntimeError("Couldn't find TESTS block in file")

    block_lines = lines[start_idx : end_idx + 1]

    # Parse existing tests
    tests = parse_tests_block(block_lines)

    # Upsert this day
    tests[day] = (p1, p2)

    # Render new block
    new_block = render_tests_block(tests)

    # Replace old block with new one
    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1 :]
    test_file.write_text("\n".join(new_lines) + "\n")


def create_solution_boilerplate(year: int, day: int) -> None:
    year_folder = get_year_folder(year)
    solution_file = year_folder / f"day{day:02d}.py"
    if not solution_file.exists():
        click.secho(f"Creating solution file {solution_file}", fg="blue")
        solution_file.write_text(SOLUTION_TEMPLATE)
    else:
        click.secho(f"Solution file already exists {solution_file}", fg="red")


def upsert_testcase(year: int, day: int, p1: int = 0, p2: int = 0) -> None:
    test_file = get_tests_file()
    logging.debug(f"Add/update test case to file {test_file}")
    lines = test_file.read_text().splitlines()

    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if line.strip().startswith("TESTS = ["):
            start_idx = i
        if start_idx is not None and line.find(f"SampleCase({year}, {day}, ") != -1:
            logging.error(f"Test case already exists for {year} day {day}!")
            return
        if start_idx is not None and line.strip().startswith("]"):
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        logging.error(f"Could not find TESTS in {test_file}!")
        return

    new_entry = f"    SampleCase({year}, {day}, {p1}, {p2}),"

    # inject before the closing bracket
    updated = lines[:end_idx] + [new_entry] + lines[end_idx:]

    test_file.write_text("\n".join(updated))
    logging.info(f"Added SampleCase({day}, {p1}, {p2})")
