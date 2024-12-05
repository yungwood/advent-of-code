# Advent of Code 2024

Here's my solutions to [Advent of Code 2024](https://adventofcode.com/2024) written in **Go**!

## Structure

Each day's solutions are stored in separate packages. Tests are provided for each package using example input.

There's also `test` and `util` modules with some common helper functions used across multiple solutions.

## How to run

```bash
# solve day 1 (both parts)
go run . --day 1 --input myinput.txt

# solve day 5 part 2 only
go run . --day 1 --part 2 --input myinput.txt

# run test for day 1
go test ./day01

# run all tests
go test ./...

# help
go run . --help
```
