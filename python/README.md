# Advent of Code

Solutions for [Advent of Code](https://adventofcode.com) written in **Python**, with a small CLI tool for running individual days and parts.

## Solutions

Solutions for each day can be found in the subfolders for each year.

Each day solutions file contains 3 functions:

- `parse` for parsing puzzle input from a string
- `part1` and `part2` for solving respective parts

Each day solution file can be run as a standalone file with puzzle input provided via stdin.

For example:

```bash
python3 2025/day01.py < input.txt
```

The `aoc` cli tool handles reading puzzle input from file/stdin and imports the day module based on flags provided. It also handles fetching puzzle text, inputs and storing them locally.

## Getting Started

### Setup development environment

```bash
# setup venv
make dev
source .venv/bin/activate
```

### Lint

```bash
make lint
```

### Run Tests

```bash
make test
```

## Using the CLI

Solve a given day with optional flags:

```bash
# solve today's puzzle part 1 (or 1st day puzzle if current month is not December)
# if no input provided via stdin or --file, will attempt to load sample input
aoc solve

# Solve day 1 part 2 specifying an input file
aoc solve --day 1 --part 2 --input input.txt

# Pipe input from stdin
aoc solve --d2 < input.txt

# Enable debug logging
aoc --debug solve -d3 -p2
```
