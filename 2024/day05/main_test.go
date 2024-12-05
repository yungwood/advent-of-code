package main

import (
	"github.com/yungwood/advent-of-code/2024/test"
	"testing"
)

const exampleInput = `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47`

func Test(t *testing.T) {
	testCases := []test.TestCase{
		{Input: exampleInput, Fn: part1, Answer: 143, Description: "Day 5 Part 1"},
		{Input: exampleInput, Fn: part2, Answer: 123, Description: "Day 5 Part 2"},
	}
	test.RunTests(t, testCases)
}
