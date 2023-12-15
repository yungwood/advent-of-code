import argparse


def order_lenses(input):
    boxes = {}
    for item in input:
        if '=' in item:
            data = item.split('=')
            lens = tuple([data[0], int(data[1])])
            box = hash(data[0])
            if box in boxes.keys() and lens[0] in [i[0] for i in boxes[box]]:
                i = [i[0] for i in boxes[box]].index(lens[0])
                boxes[box][i] = lens
            else:
                if box in boxes.keys():
                    boxes[box].append(lens)
                else:
                    boxes[box] = [lens]
        if '-' in item:
            lens_type = item.strip('-')
            box = hash(lens_type)
            if box in boxes.keys() and lens_type in [i[0] for i in boxes[box]]:
                i = [i[0] for i in boxes[box]].index(lens_type)
                boxes[box].pop(i)
    return boxes


def hash(input):
    value = 0
    for char in input:
        value += ord(char)
        value = value * 17 % 256
    return value


def main():
    # script args
    parser = argparse.ArgumentParser(description='Advent of Code 2023: Day 15')
    parser.add_argument('filename', help='File containing the puzzle input')
    args = parser.parse_args()

    # process puzzle input
    with open(args.filename) as file:
        puzzle_input = file.read()
    puzzle_data = puzzle_input.split(',')

    # calculate answer for part 1
    answer1 = 0
    for item in puzzle_data:
        answer1 += hash(item)
    print('Answer for Part 1:', answer1)

    answer2 = 0
    box_map = order_lenses(puzzle_data)
    for i, box in box_map.items():
        for j, lens in enumerate(box, 1):
            answer2 += (i + 1) * j * lens[1]
    print('Answer for Part 2:', answer2)


if __name__ == "__main__":
    main()
