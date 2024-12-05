package main

import (
	"github.com/yungwood/advent-of-code/2024/test"
	"testing"
)

const exampleInput1 = `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
const exampleInput2 = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput1, Fn: part1, Answer: 161, Description: "Day 3 Part 1"},
		{Input: exampleInput2, Fn: part2, Answer: 48, Description: "Day 3 Part 2"},
	}
	test.RunTests(t, testCases)
}
