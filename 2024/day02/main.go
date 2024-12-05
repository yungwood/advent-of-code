package day02

import (
	"github.com/yungwood/advent-of-code/2024/util"
)

func Part1(input string) int {
	count := 0
	reactorReadings := util.ParseIntGrid(input, " ")
	for _, item := range reactorReadings {
		if isReactorSafe(item) {
			count++
		}
	}
	return count
}

func Part2(input string) int {
	count := 0
	reactorReadings := util.ParseIntGrid(input, " ")
	for _, item := range reactorReadings {
		if isReactorSafeWithDampener(item) {
			count++
		}
	}
	return count
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
