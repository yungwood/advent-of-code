package util

import (
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
)

func ReadFile(filename string) string {
	// Get the file and line number of the caller
	_, callerFile, _, ok := runtime.Caller(1)
	if !ok {
		panic("Failed to retrieve caller information")
	}
	// Resolve full path to the target file
	callerDir := filepath.Dir(callerFile)
	fullPath := filepath.Join(callerDir, filename)
	// Read the file
	data, err := os.ReadFile(fullPath)
	if err != nil {
		panic(err)
	}
	// Return content as string (trim trailing newlines)
	content := string(data)
	return strings.TrimRight(content, "\n")
}

// ParseIntegerList takes a string of space separated numbers
// and returns an array of integers
func ParseIntegerList(input string) []int {
	items := strings.Split(input, " ")
	parsed := []int{}
	for _, item := range items {
		value, err := strconv.Atoi(item)
		if err != nil {
			panic(err)
		}
		parsed = append(parsed, value)
	}
	return parsed
}

// ParseRuneGrid takes a string with a grid and creates a 2d slice
// of runes
func ParseRuneGrid(input string) [][]rune {
	lines := strings.Split(input, "\n") // split lines
	grid := make([][]rune, len(lines))  // create grid of correct length
	for i, line := range lines {
		grid[i] = []rune(line) // convert each line to slice of runes
	}
	return grid
}
