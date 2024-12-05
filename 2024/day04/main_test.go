package main

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"testing"
)

func TestExample(t *testing.T) {
	input := util.ReadFile("example.txt")
	expected := 18
	result := part1(input)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 9
	result = part2(input)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}

func Test(t *testing.T) {
	input := util.ReadFile("input.txt")
	expected := 2464
	result := part1(input)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 1982
	result = part2(input)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}
