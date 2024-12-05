package main

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"testing"
)

func TestExample(t *testing.T) {
	input := util.ReadFile("example.txt")
	expected := 143
	result := part1(input)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 123
	result = part2(input)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}
