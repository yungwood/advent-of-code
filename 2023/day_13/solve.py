import argparse


# parse data to list of lists
def parse_data(input):
    parsed = []
    for map_string in input.split('\n\n'):
        data = map_string.split('\n')
        parsed.append(data)
    return parsed


# rotate x/y on map and then process with existing y functions
def get_x_reflection(map_data, smudges):
    rotated_map = ["" for i in range(len(map_data[0]))]
    for row_data in map_data:
        for i, char in enumerate(row_data):
            rotated_map[i] += char
    return get_y_reflection(rotated_map, smudges)


# test for reflection at each possible y value
def get_y_reflection(map_data, smudges):
    for y in range(len(map_data) - 1):
        if validate_y_reflection(y, map_data, smudges):
            return y + 1
    return None


# recursively validate if a reflection occurs at y
# require smudges count to match
def validate_y_reflection(y, map_data, smudges):
    if len(map_data) < 2 or y < 0 or y + 2 > len(map_data):
        return smudges == 0
    if map_data[y] == map_data[y + 1]:
        return validate_y_reflection(y - 1,
                                     [*map_data[:y], *map_data[y + 2:]],
                                     smudges)
    if smudges:
        if sum(map_data[y][i] != map_data[y + 1][i]
               for i in range(len(map_data[y]))
               ) == 1:
            return validate_y_reflection(y - 1,
                                         [*map_data[:y], *map_data[y + 2:]],
                                         smudges - 1)
    return False


def main():
    # parse script args
    parser = argparse.ArgumentParser(description='Advent of Code 2023: Day 13')
    parser.add_argument('filename', help='File containing the puzzle input')
    args = parser.parse_args()

    # process puzzle input file
    with open(args.filename) as file:
        puzzle_input = file.read()

    # parse ash/rock map data
    parsed_map_data = parse_data(puzzle_input)

    print(parsed_map_data)

    # calculate answer for part 1
    answer = 0
    for index, map_data in enumerate(parsed_map_data, 1):
        x_reflection = get_x_reflection(map_data, 0)
        if x_reflection:
            answer += x_reflection
            continue
        y_reflection = get_y_reflection(map_data, 0)
        if y_reflection:
            answer += y_reflection * 100
            continue
    print("The answer for part 1 is {}".format(answer))

    # calculate answer for part 2
    answer = 0
    for index, map_data in enumerate(parsed_map_data, 1):
        x_reflection = get_x_reflection(map_data, 1)
        if x_reflection:
            answer += x_reflection
            continue
        y_reflection = get_y_reflection(map_data, 1)
        if y_reflection:
            answer += y_reflection * 100
            continue
    print("The answer for part 2 is {}".format(answer))


if __name__ == "__main__":
    main()
