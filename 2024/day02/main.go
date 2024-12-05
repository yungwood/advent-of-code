package main

import (
	"fmt"
	"strings"

	"github.com/yungwood/advent-of-code/2024/util"
)

func main() {
	// read and parse input
	input := util.ReadFile("input.txt")
	reactorReadings := parseInput(input)
	answer1 := part1(reactorReadings)
	fmt.Println("The answer for part 1 is:", answer1)
	answer2 := part2(reactorReadings)
	fmt.Println("The answer for part 2 is:", answer2)
}

func part1(reactorReadings [][]int) int {
	count := 0
	for _, item := range reactorReadings {
		if isReactorSafe(item) {
			count++
		}
	}
	return count
}

func part2(reactorReadings [][]int) int {
	count := 0
	for _, item := range reactorReadings {
		if isReactorSafeWithDampener(item) {
			count++
		}
	}
	return count
}

func parseInput(input string) [][]int {
	lines := strings.Split(input, "\n")
	reactorReadings := [][]int{}
	for _, line := range lines {
		row := util.ParseIntegerList(line)
		reactorReadings = append(reactorReadings, row)
	}
	return reactorReadings
}

func isReactorSafeWithDampener(input []int) bool {
	if isReactorSafe(input) {
		return true
	}
	for i := range input {
		combination := append([]int{}, input[:i]...)
		combination = append(combination, input[i+1:]...)
		if isReactorSafe(combination) {
			return true
		}

	}

	return false
}

func isReactorSafe(input []int) bool {
	ascending := input[0] < input[1]
	for i := 0; i < len(input)-1; i++ {
		// values cannot be repeated
		if input[i] == input[i+1] {
			return false
		}
		// calculate difference
		difference := input[i] - input[i+1]
		if ascending {
			difference = -difference
		}
		// difference must be between 1 and 3
		if difference < 1 || difference > 3 {
			return false
		}
	}
	return true
}
