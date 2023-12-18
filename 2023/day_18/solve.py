import argparse


direction_map = {
    'U': [0, -1], 'D': [0, 1], 'R': [1, 0], 'L': [-1, 0],
    '0': [1, 0], '1': [0, 1], '2': [-1, 0], '3': [0, -1]
}


def parse_dig_data_part1(puzzle_input):
    data = []
    for line in puzzle_input.split("\n"):
        parsed = line.split(' ')
        data.append([parsed[0], int(parsed[1])])
    return data


def parse_dig_data_part2(puzzle_input):
    data = []
    for line in puzzle_input.split("\n"):
        parsed = line.split(' ')
        distance = int(parsed[2][2:-2], 16)
        direction = parsed[2][-2:-1]
        data.append([direction, distance])
    return data


def get_points(dig_data):
    data = [tuple([0, 0])]
    for dig in dig_data:
        location = data[-1]
        step = [i * dig[1] for i in direction_map[dig[0]]]
        data.append(tuple([location[0] + step[0], location[1] + step[1]]))
    return data


def calc_fill_area(points):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(points) - 1):
        sum1 += points[i][0] * points[i + 1][1]
        sum2 += points[i][1] * points[i + 1][0]
    area = abs(sum1 - sum2) / 2
    return int(area)


def calc_perimeter_length(dig_data):
    perimeter = 0
    for dig in dig_data:
        perimeter += dig[1]
    return perimeter


def calc_answer(dig_data):
    perimeter = calc_perimeter_length(dig_data) / 2 + 1
    points = get_points(dig_data)
    fill_area = calc_fill_area(points)
    return int(perimeter + fill_area)


def main():
    # script args
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 18")
    parser.add_argument("filename", help="File containing the puzzle input")
    args = parser.parse_args()

    # process puzzle input
    with open(args.filename) as file:
        puzzle_input = file.read()

    # answer part 1
    dig_data = parse_dig_data_part1(puzzle_input)
    answer1 = calc_answer(dig_data)
    print("Answer for Part 1:", answer1)

    # answer part 1
    dig_data = parse_dig_data_part2(puzzle_input)
    answer2 = calc_answer(dig_data)
    print("Answer for Part 2:", answer2)


if __name__ == "__main__":
    main()
