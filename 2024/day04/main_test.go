package day04

import (
	"github.com/yungwood/advent-of-code/2024/test"
	"testing"
)

const exampleInput = `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput, Fn: Part1, Answer: 18, Description: "Day 4 Part 1"},
		{Input: exampleInput, Fn: Part2, Answer: 9, Description: "Day 4 Part 2"},
	}
	test.RunTests(t, testCases)
}
