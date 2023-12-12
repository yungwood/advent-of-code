import argparse
from functools import cache

# parse script args
parser = argparse.ArgumentParser(description='Advent of Code 2023: Day 12')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# parse data to list of lists
def parse_data(input):
    parsed = []
    for line in input.split('\n'):
        data = line.split(' ')
        springs = data[0]
        # groups need to be tuple instead of list to be hashable for cache
        groups = tuple(int(x) for x in data[1].split(','))
        parsed.append([springs, groups])
    return parsed


# find the number of possible solutions by looping through the input data
# char by char using recursion at branch points (?) as required
# use python cache decorator to speed things up
@cache
def get_solution_count(springs, groups):

    solution_count = 0

    # ignore '.'
    springs = springs.lstrip('.')

    # if no more groups to process then
    # we can check to make sure no more # remain
    if not groups:
        if not springs:
            return 1
        if '#' not in springs:
            return 1
        return 0

    # if no string left with groups
    if not springs:
        return 0

    # get first character
    char = springs[0]

    # if it's a broken spring, see what's required
    if char == '#':
        # check length is enough for group
        if len(springs) < groups[0]:
            return 0
        # check if working spring is within next group size
        if '.' in springs[:groups[0]]:
            return 0
        # check to see if we are at the end of the string
        if len(springs) == groups[0]:
            # check if there are more groups required
            if len(groups) > 1:
                return 0
            # we already checked for '.' so remaining group must be '#'
            # (or '?' which need to become '#')
            return 1
        # make sure next char after group is not another broken spring
        if springs[groups[0]] == '#':
            return 0
        # if next char after group is '?' then we can only use '.'
        # strip off the current group and do it all again
        return get_solution_count('.' + springs[groups[0] + 1:], groups[1:])

    # we stripped all leading '.' so next char must be '?'
    # try both options
    solution_count += get_solution_count('#' + springs[1:], groups)
    solution_count += get_solution_count('.' + springs[1:], groups)
    return solution_count


# process puzzle input file
with open(args.filename) as file:
    puzzle_input = file.read()

# parse spring data
spring_data = parse_data(puzzle_input)

# calculate answer for part 1
answer = 0
for item in spring_data:
    answer += get_solution_count(item[0], item[1])
print("Than answer for part 1 is {}".format(answer))

# calculate answer for part 2
answer = 0
for item in spring_data:
    answer += get_solution_count(((item[0] + '?') * 4) + item[0], item[1] * 5)
print("Than answer for part 2 is {}".format(answer))
