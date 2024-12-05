package day03

import (
	"regexp"
	"strconv"
	"strings"
)

func Part1(input string) int {
	total := 0
	instructions := getInstructions(input)
	for _, instruction := range instructions {
		total = total + (instruction.a * instruction.b)
	}
	return total
}

func Part2(input string) int {
	total := 0
	instructions := getInstructions(input)
	enabled := true
	for _, instruction := range instructions {
		if instruction.op != "mul" {
			enabled = instruction.op == "do"
		}
		if enabled {
			total = total + (instruction.a * instruction.b)
		}
	}
	return total
}

type Instruction struct {
	a, b int
	op   string
}

func getInstructions(input string) []Instruction {
	pattern := `(?:(mul)\((\d{1,3})\,(\d{1,3})\)|do\(\)|don't\(\))`
	re := regexp.MustCompile(pattern)
	matches := re.FindAllStringSubmatch(input, -1)
	instructions := []Instruction{}
	for _, match := range matches {
		if match[1] != "mul" {
			instructions = append(instructions, Instruction{a: 0, b: 0, op: strings.TrimRight(match[0], "()")})
			continue
		}
		a, err := strconv.Atoi(match[2])
		if err != nil {
			panic(err)
		}
		b, err := strconv.Atoi(match[3])
		if err != nil {
			panic(err)
		}
		instructions = append(instructions, Instruction{a: a, b: b, op: match[1]})
	}
	return instructions
}
