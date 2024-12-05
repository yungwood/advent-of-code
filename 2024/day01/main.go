package main

import (
	"fmt"
	"github.com/yungwood/advent-of-code/2024/util"
	"math"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// read and parse input to lists
	input := util.ReadFile("input.txt")
	list1, list2 := parseInput(input)

	// calculate part1
	answer1 := part1(list1, list2)
	fmt.Println("The answer for part 1 is:", answer1)

	// calculate part2
	answer2 := part2(list1, list2)
	fmt.Println("The answer for part 2 is:", answer2)
}

func part1(list1, list2 []int) int {
	// create a results array
	results := make([]int, len(list1))
	// calculate differences
	for i := 0; i < len(list1); i++ {
		results[i] = int(math.Abs(float64(list1[i] - list2[i])))
	}
	return sumArray(results)
}

func part2(list1, list2 []int) int {
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
