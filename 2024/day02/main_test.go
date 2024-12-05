package main

import (
	"github.com/yungwood/advent-of-code/2024/test"
	"testing"
)

const exampleInput = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput, Fn: part1, Answer: 2, Description: "Day 2 Part 1"},
		{Input: exampleInput, Fn: part2, Answer: 4, Description: "Day 2 Part 2"},
	}
	test.RunTests(t, testCases)
}
