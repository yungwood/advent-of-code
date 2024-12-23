package day05

import (
	"github.com/yungwood/advent-of-code/2024/util"
	"slices"
)

func Part1(input string) int {
	data := util.ParseChunks(input)
	rules := util.ParseIntGrid(data[0], "|")
	jobs := util.ParseIntGrid(data[1], ",")
	total := 0
	for _, job := range jobs {
		if evaluatePrint(job, rules) {
			total += job[len(job)/2]
		}
	}
	return total
}

func Part2(input string) int {
	data := util.ParseChunks(input)
	rules := util.ParseIntGrid(data[0], "|")
	jobs := util.ParseIntGrid(data[1], ",")
	total := 0
	for _, job := range jobs {
		if !evaluatePrint(job, rules) {
			fixedJob := fixPrint(job, rules)
			total += fixedJob[len(fixedJob)/2]
		}
	}
	return total
}

func evaluatePrint(job []int, rules [][]int) bool {
	for _, rule := range rules {
		a := slices.Index(job, rule[0])
		b := slices.Index(job, rule[1])
		if a < 0 || b < 0 {
			continue
		}
		if a > b {
			return false
		}
	}
	return true
}

func fixPrint(job []int, rules [][]int) []int {
	fixes := 0
	for {
		fixes = 0
		// evaluate rules
		for _, rule := range rules {
			a := slices.Index(job, rule[0])
			b := slices.Index(job, rule[1])
			if a < 0 || b < 0 {
				continue
			}
			if a > b {
				// move item from index b to index a
				job = util.MoveIntSlice(job, a, b)
				fixes++
			}
		}
		// if no fixes were required this loop our print job is fixed!
		if fixes == 0 {
			break
		}
	}
	return job
}
