import argparse


def rotate_map(map_data, reverse):
    if reverse:
        rotated_list = list(reversed(list(zip(*map_data))))
    else:
        rotated_list = list(zip(*map_data[::-1]))
    return ["".join(column) for column in rotated_list]


def tilt(map_data):
    data = []
    for column in map_data:
        data.append('#'.join([
            ''.join(sorted(value, reverse=True))
            for value in column.split('#')
            ]))
    return data


def spin_map(map_data):
    for i in range(4):
        map_data = tilt(map_data)
        map_data = rotate_map(map_data, False)
    return map_data


def calc_total_load(map_data):
    total_load = 0
    for map in map_data:
        for weight, char in enumerate(reversed(map), 1):
            if char == 'O':
                total_load += weight
    return total_load


def main():
    # script args
    parser = argparse.ArgumentParser(description='Advent of Code 2023: Day 14')
    parser.add_argument('filename', help='File containing the puzzle input')
    args = parser.parse_args()

    # process puzzle input
    with open(args.filename) as file:
        puzzle_input = file.read()
    puzzle_data = [line for line in puzzle_input.split('\n')]

    # calculate answer for part 1
    map_data = rotate_map(puzzle_data, True)
    map_data = tilt(map_data)
    answer1 = calc_total_load(map_data)
    print('Answer for Part 1:', answer1)

    # calculate answer for part 2
    # find where value loops then work out last map_data
    seen = []
    map_data = rotate_map(puzzle_data, True)
    spins = 1000000000
    for i in range(spins):
        map_data = spin_map(map_data)
        map_string = "|".join(map_data)
        if map_string in seen:
            start_offset = seen.index(map_string)
            loop_length = i - seen.index(map_string)
            loop_modulus = (spins - 1 - start_offset) % loop_length
            map_data = seen[start_offset + loop_modulus].split("|")
            break
        else:
            seen.append(map_string)
    answer2 = calc_total_load(map_data)
    print('Answer for Part 2:', answer2)


if __name__ == "__main__":
    main()
