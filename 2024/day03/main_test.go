package main

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"testing"
)

func TestExample(t *testing.T) {
	data := util.ReadFile("example1.txt")
	expected := 161
	result := part1(data)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	data = util.ReadFile("example2.txt")
	expected = 48
	result = part2(data)
	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}

}

func Test(t *testing.T) {
	data := util.ReadFile("input.txt")
	expected := 166357705
	result := part1(data)
	if result != expected {
		t.Errorf("Part 1: Expected %d, got %d", expected, result)
	}
	expected = 88811886
	result = part2(data)

	if result != expected {
		t.Errorf("Part 2: Expected %d, got %d", expected, result)
	}
}
