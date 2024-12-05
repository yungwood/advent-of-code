package day01

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

func Part1(input string) int {
	list1, list2 := parseInput(input)
	// create a results array
	results := make([]int, len(list1))
	// calculate differences
	for i := 0; i < len(list1); i++ {
		results[i] = int(math.Abs(float64(list1[i] - list2[i])))
	}
	return sumArray(results)
}

func Part2(input string) int {
	list1, list2 := parseInput(input)
	result := 0
	for _, num := range list1 {
		result += num * countOccurrences(num, list2)
	}
	return result
}

func parseInput(input string) ([]int, []int) {
	var colA, colB []int

	lines := strings.Split(input, "\n")

	for _, line := range lines {

		parts := strings.Fields(line)

		a, err1 := strconv.Atoi(parts[0])
		b, err2 := strconv.Atoi(parts[1])
		if err1 != nil || err2 != nil {
			panic(fmt.Sprintf("Failed to parse integers in line %s", line))
		}

		colA = append(colA, a)
		colB = append(colB, b)
	}

	// sort from smallest to largest
	sort.Ints(colA)
	sort.Ints(colB)

	return colA, colB
}

func sumArray(arr []int) int {
	sum := 0
	for _, num := range arr {
		sum += num
	}
	return sum
}

func countOccurrences(needle int, haystack []int) int {
	count := 0
	for _, num := range haystack {
		if num == needle {
			count++
		}
	}
	return count
}
