package main

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"testing"
)

func TestExample(t *testing.T) {
	input := util.ReadFile("example.txt")
	list1, list2 := parseInput(input)
	expected := 11
	result := part1(list1, list2)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 31
	result = part2(list1, list2)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}

}

func Test(t *testing.T) {
	input := util.ReadFile("input.txt")
	list1, list2 := parseInput(input)
	expected := 3508942
	result := part1(list1, list2)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 26593248
	result = part2(list1, list2)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}
