package grids

import (
	"fmt"
	"strings"
)

type Direction struct {
	Step [2]int
	Rune rune
}

func (point Point) Equals(compare Point) bool {
	return point.X == compare.X && point.Y == compare.Y
}

type Point struct {
	X int
	Y int
}

func (haystack Path) Find(needle Point) int {
	for i, point := range haystack.Path {
		if needle.Equals(point) {
			return i
		}
	}
	return -1
}

type Path struct {
	Path []Point
}

// finds a rune within a grid and returns first match
func (grid RuneGrid) FindRune(find rune, limit int) []Point {
	results := []Point{}
	for y, row := range grid.Data {
		for x, rune := range row {
			if rune == find {
				results = append(results, Point{x, y})
				if len(results) == limit {
					return results
				}
			}
		}
	}
	return results
}

// print the grid to stdout
func (grid RuneGrid) Print() {
	for _, row := range grid.Data {
		fmt.Println(string(row))
	}
}

// Generate a string representation of a Path for comparison
func (p Path) String() string {
	var sb strings.Builder
	for _, point := range p.Path {
		sb.WriteString(fmt.Sprintf("(%d,%d)", point.X, point.Y))
	}
	return sb.String()
}

// DeepCopy creates a deep copy of a RuneGrid
func (grid RuneGrid) DeepCopy() RuneGrid {
	// Create a new slice of slices with the same length as the original
	newData := make([][]rune, len(grid.Data))

	// Copy each inner slice
	for i, innerSlice := range grid.Data {
		newData[i] = append([]rune(nil), innerSlice...) // Copy the inner slice
	}

	// Return a new RuneGrid with the copied data
	return RuneGrid{Data: newData}
}

type RuneGrid struct {
	Data [][]rune
}

// ParseRuneGrid takes a string with a grid and creates a 2d slice
// of runes
func NewRuneGrid(input string) RuneGrid {
	lines := strings.Split(input, "\n") // split lines
	data := make([][]rune, len(lines))  // create grid
	for i, line := range lines {
		data[i] = []rune(line) // convert each line to slice of runes
	}
	return RuneGrid{
		Data: data,
	}
}
