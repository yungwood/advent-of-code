package day01

import (
	"github.com/yungwood/advent-of-code/2024/test"
	"testing"
)

const exampleInput = `3   4
4   3
2   5
1   3
3   9
3   3`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput, Fn: Part1, Answer: 11, Description: "Day 1 Part 1"},
		{Input: exampleInput, Fn: Part2, Answer: 31, Description: "Day 1 Part 2"},
	}
	test.RunTests(t, testCases)
}
