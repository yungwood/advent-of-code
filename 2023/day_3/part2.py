import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# return an array with location of each star on a line
def get_gears(input):
    # find all gears
    results = re.finditer(r"(\*)", input)
    # save location of gears to array
    gears = []
    for match in results:
        gears.append(match.start())
    return gears


# return a dict with each number match as key and span for value
def get_numbers(input):
    # find all numbers
    results = re.finditer(r"(\d+)", input)
    # save location of gears to array
    numbers = []
    for match in results:
        numbers.append([match.group(), match.span()])
    return numbers


# check if a number is located near a gear
def get_adjacent_numbers(numbers_map, line_no, location):
    adjacent_numbers = []
    # test line before gear
    if line_no > 0:
        for number_item in numbers_map[(line_no - 1)]:
            if number_item[1][0] <= location + 1 and \
               number_item[1][1] >= location:
                adjacent_numbers.append(int(number_item[0]))
    # test line of gear
    for number_item in numbers_map[line_no]:
        if number_item[1][0] == location + 1 or number_item[1][1] == location:
            adjacent_numbers.append(int(number_item[0]))
    # test for line after gear
    if line_no < len(numbers_map) - 1:
        for number_item in numbers_map[(line_no + 1)]:
            if number_item[1][0] <= location + 1 and \
               number_item[1][1] >= location:
                adjacent_numbers.append(int(number_item[0]))

    return adjacent_numbers


# process puzzle input file
with open(args.filename) as file:

    # create a dict with every line and location of stars
    gear_map = {}
    # create a dict with every line and numbers/spans
    numbers_map = {}
    for line_count, line in enumerate(file):
        gear_map[line_count] = get_gears(line.rstrip('\n'))
        numbers_map[line_count] = get_numbers(line.rstrip('\n'))

    sum = 0

    for line_no, gears in gear_map.items():
        for gear in gears:
            adjacent_numbers = get_adjacent_numbers(numbers_map, line_no, gear)
            if len(adjacent_numbers) == 2:
                sum += (adjacent_numbers[0] * adjacent_numbers[1])

    # print answer
    print("The answer is {}!".format(sum))
