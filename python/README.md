# Advent of Code

Solutions for [Advent of Code](https://adventofcode.com) written in **Python**, with a small CLI tool for running individual days and parts.

## Solutions

Solutions for each day can be found in [`aoc/solutions/`](./aoc/solutions/) with subfolders for each year.

Each day solutions file contains 3 functions:

- `parse` for parsing puzzle input from a string
- `part1` and `part2` for solving respective parts

Each day solution file can be run as a standalone file with puzzle input provided via stdin.

For example:

```bash
python3 aoc/2025/day01.py < input.txt
```

The `aoc` cli tool handles reading puzzle input from file/stdin and imports the day module based on flags provided.

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
# Solve day 1 part 2 using an input file
aoc solve 1 --part 2 --input myinput.txt

# Pipe input from stdin
cat myinput.txt | aoc solve 2

# Enable debug logging
aoc --debug solve 3
```
