# Advent of Code Solutions in Python

Solutions for [Advent of Code](https://adventofcode.com) written in **Python**, plus a small CLI tool to help with development.

## Solutions

Solutions for each day can be found in the subfolders for each year.

Each day solutions file contains 3 functions:

- `parse` for parsing puzzle input from a string
- `part1` and `part2` for solving respective parts

Each day solution file can be run as a standalone file with puzzle input provided via stdin.

For example:

```bash
# find solutions for 2025 day 1
python3 2025/day01.py < input.txt
```

## Advent of Code CLI

The `aoc` cli tool handles reading puzzle input from file/stdin and imports the day module based on flags provided. It also handles fetching puzzle text, inputs and storing them locally.

### Getting Started

Setup development environment:

```bash
# setup venv
make dev
source .venv/bin/activate
```

Run linting:

```bash
make lint
```

Run tests:

```bash
make test
```

### Using the CLI

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
