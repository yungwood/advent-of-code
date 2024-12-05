package day04

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"strconv"
)

func Part1(input string) int {
	grid := util.ParseRuneGrid(input)
	results := [][4]int{}
	directions := [][2]int{
		{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}, // all directions
	}
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[y]); x++ {
			results = append(results, findAllMatches(grid, "XMAS", x, y, directions)...)
		}
	}
	return len(results)
}

func Part2(input string) int {
	grid := util.ParseRuneGrid(input)
	results := [][4]int{}
	for y := 0; y < len(grid); y++ {
		directions := [][2]int{
			{1, 1}, {1, -1}, {-1, 1}, {-1, -1}, // diagonal only
		}
		for x := 0; x < len(grid[y]); x++ {
			results = append(results, findAllMatches(grid, "MAS", x, y, directions)...)
		}
	}
	centrePoints := []string{}
	for _, result := range results {
		centrePoints = append(centrePoints, strconv.Itoa(result[0]+result[2])+","+strconv.Itoa(result[1]+result[3]))
	}
	occurrences := make(map[string]int)
	for _, point := range centrePoints {
		occurrences[point]++
	}
	count := 0
	for _, occurrence := range occurrences {
		if occurrence > 1 {
			count++
		}
	}
	return count
}

// fans out recursive search of grid for taget in given directions starting from point x, y
func findAllMatches(grid [][]rune, target string, x, y int, directions [][2]int) [][4]int {
	results := [][4]int{}
	for _, direction := range directions {
		if findResult(grid, target, x, y, 0, direction[0], direction[1]) {
			results = append(results, [4]int{x, y, direction[0], direction[1]})
		}
	}
	return results
}

// recursively search for sequence of targetString
func findResult(grid [][]rune, target string, x, y, targetIndex, xMove, yMove int) bool {
	// check if still in grid
	if x < 0 || y < 0 || y >= len(grid) || x >= len(grid[y]) {
		return false
	}
	// check for match
	if rune(target[targetIndex]) != grid[y][x] {
		return false
	}
	// see if this is the last char
	if targetIndex == len(target)-1 {
		return true
	}
	// continue search
	return findResult(grid, target, x+xMove, y+yMove, targetIndex+1, xMove, yMove)
}
