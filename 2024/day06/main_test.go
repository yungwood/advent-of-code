package day06

import (
	"testing"

	"github.com/yungwood/advent-of-code/2024/test"
)

const exampleInput = `....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput, Fn: Part1, Answer: 41, Description: "Day 6 Part 1"},
		{Input: exampleInput, Fn: Part2, Answer: 6, Description: "Day 6 Part 2"},
	}
	test.RunTests(t, testCases)
}
