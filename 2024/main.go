package main

import (
	"flag"
	"fmt"
	"os"
	"time"

	"github.com/yungwood/advent-of-code/2024/day01"
	"github.com/yungwood/advent-of-code/2024/day02"
	"github.com/yungwood/advent-of-code/2024/day03"
	"github.com/yungwood/advent-of-code/2024/day04"
	"github.com/yungwood/advent-of-code/2024/day05"
	"github.com/yungwood/advent-of-code/2024/day06"
	"github.com/yungwood/advent-of-code/2024/util"
)

func main() {
	// command flags
	var (
		inputFile string
		day, part int
	)
	flag.StringVar(&inputFile, "input", "input.txt", "file containing puzzle input")
	flag.IntVar(&day, "day", 0, "day (required)")
	flag.IntVar(&part, "part", 0, "part (optional)")
	flag.Parse()

	// map days and parts to fns
	fns := map[int]map[int]func(string) int{
		1: {1: day01.Part1, 2: day01.Part2},
		2: {1: day02.Part1, 2: day02.Part2},
		3: {1: day03.Part1, 2: day03.Part2},
		4: {1: day04.Part1, 2: day04.Part2},
		5: {1: day05.Part1, 2: day05.Part2},
		6: {1: day06.Part1, 2: day06.Part2},
	}

	if day == 0 {
		fmt.Println("ERROR: Please specify day using --day")
		os.Exit(0)
	}

	input := util.ReadFile(inputFile)

	if parts, ok := fns[day]; ok {
		fmt.Printf("Solving puzzle for day 1 using %s\n", inputFile)
		if part == 0 {
			for i, fn := range parts {
				fmt.Printf("The answer for part %d is: ", i)
				solve(input, fn)
			}
		} else if fn, ok := parts[part]; ok {
			fmt.Printf("The answer for part %d is: ", part)
			solve(input, fn)
		} else {
			fmt.Printf("Part %d for day %d not found!\n", part, day)
			os.Exit(1)
		}
	} else {
		fmt.Printf("Day %d not found!\n", day)
		os.Exit(1)
	}
}

func solve(input string, fn func(string) int) {
	start := time.Now()
	answer := fn(input)
	elapsed := time.Since(start)
	fmt.Printf("%d (took %s)\n", answer, elapsed)
}
