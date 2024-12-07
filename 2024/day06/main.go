package day06

import (
	"github.com/yungwood/advent-of-code/2024/util/grids"
)

func Part1(input string) int {
	grid := grids.NewRuneGrid(input)
	walkedMap := walkMap(grid)
	results := walkedMap.FindRune(rune('X'), 0)
	return len(results)
}

func Part2(input string) int {
	grid := grids.NewRuneGrid(input)
	var results []grids.Path
	findstart := grid.FindRune(rune('^'), 1)
	start := findstart[0]
	path := grids.Path{Path: []grids.Point{start}}
	var directions = []grids.Direction{
		{Step: [2]int{0, -1}, Rune: rune('^')},
		{Step: [2]int{1, 0}, Rune: rune('>')},
		{Step: [2]int{0, 1}, Rune: rune('v')},
		{Step: [2]int{-1, 0}, Rune: rune('<')},
	}
	walk(grid, directions, path, false, &results)
	return len(results)
}

func walkMap(grid grids.RuneGrid) grids.RuneGrid {
	var directions = []grids.Direction{
		{Step: [2]int{0, -1}, Rune: rune('^')},
		{Step: [2]int{1, 0}, Rune: rune('>')},
		{Step: [2]int{0, 1}, Rune: rune('v')},
		{Step: [2]int{-1, 0}, Rune: rune('<')},
	}

	results := grid.FindRune(rune('^'), 1)
	location := results[0]
	for {
		// check directions in order
		for turn, direction := range directions {
			newLocation := grids.Point{X: location.X + direction.Step[0], Y: location.Y + direction.Step[1]}
			// if out of bounds we are done
			grid.Data[location.Y][location.X] = rune('X')
			if newLocation.X < 0 || newLocation.Y < 0 || newLocation.X >= len(grid.Data) || newLocation.Y >= len(grid.Data[0]) {
				return grid
			}
			// check next rune
			if grid.Data[newLocation.Y][newLocation.X] != rune('#') {
				// rotate directions
				if turn > 0 {
					directions = append(directions[turn:], directions[:turn]...)
				}
				grid.Data[newLocation.Y][newLocation.X] = direction.Rune
				location = newLocation
				break
			}
		}
	}
}

// TODO: refactor this because it kind of sucks?
func walk(grid grids.RuneGrid, directions []grids.Direction, path grids.Path, changed bool, results *[]grids.Path) {
	location := path.Path[len(path.Path)-1]
	// check directions in order
	for turn, direction := range directions {
		newLocation := grids.Point{X: location.X + direction.Step[0], Y: location.Y + direction.Step[1]}
		// if out of bounds we failed
		if newLocation.X < 0 || newLocation.Y < 0 || newLocation.X >= len(grid.Data) || newLocation.Y >= len(grid.Data[0]) {
			return
		}
		// check next rune
		if grid.Data[newLocation.Y][newLocation.X] != rune('#') {
			grid.Data[newLocation.Y][newLocation.X] = rune(direction.Rune)
			// rotate directions
			if turn > 0 {
				directions = append(directions[turn:], directions[:turn]...)
			}
			lastSeen := path.Find(newLocation)
			// test adding an obstacle
			if !changed && turn < 3 && lastSeen < 0 {
				newGrid := grid.DeepCopy()
				newGrid.Data[newLocation.Y][newLocation.X] = rune('#')
				walk(newGrid, directions, path, true, results)
			}
			// test for loop
			if lastSeen > 0 {
				if path.Path[lastSeen-1].Equals(path.Path[len(path.Path)-1]) {
					*results = append(*results, path)
					return
				}
			}
			// keep walking
			path.Path = append(path.Path, newLocation)
			walk(grid, directions, path, changed, results)
			return
		}
	}
}
