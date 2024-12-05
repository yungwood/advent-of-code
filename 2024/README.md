# Advent of Code 2024

Here's my solutions to [Advent of Code 2024](https://adventofcode.com/2024) written in **Go**!

## Structure

Each day's solutions are stored in a separate folder, along with:
- **`example.txt`** - the example input provided with the challenge
- **`input.txt`** - my actual puzzle input
- **`main.go`** - the solution for the challenge
- **`main_test.go`** - tests to verify both example and actual inputs

There's also a `util` module with some common helper functions used across multiple solutions.

## How to run

To run a solution for a given day:

```bash
# run solution for day 1
go run ./day01

# test example and actual solutions for day 1
go test ./day01

# run tests for all days
go test ./day...
```

