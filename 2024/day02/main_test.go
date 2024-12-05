package main

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"testing"
)

func TestExample(t *testing.T) {
	input := util.ReadFile("example.txt")
	data := parseInput(input)
	expected := 2
	result := part1(data)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 4
	result = part2(data)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}

}

func Test(t *testing.T) {
	input := util.ReadFile("input.txt")
	data := parseInput(input)
	expected := 686
	result := part1(data)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 717
	result = part2(data)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}
