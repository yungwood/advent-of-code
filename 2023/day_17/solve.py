import argparse
from collections import defaultdict
from heapq import heappop, heappush


direction_map = {
    'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)
}


def dijsktra(map_data, start_location=(0, 0), end_location=None,
             length_min=0, length_max=0):
    x_max = len(map_data[0]) - 1
    y_max = len(map_data) - 1
    heat_loss_map = [[defaultdict(lambda: float('inf'))
                     for _ in range(0, x_max + 1)]
                     for _ in range(0, y_max + 1)]
    if not end_location:
        end_location = (x_max, y_max)
    queue = [(0, start_location, (0, 0), 0)]
    while queue:

        item = heappop(queue)
        location = item[1]
        prev_offset = item[2]
        heat_loss = item[0]
        length = item[3]

        # check to see if we are at finish
        if location == end_location:
            if length_min and length < length_min:
                continue
            return heat_loss

        # add neighbors to queue
        for direction, offset in direction_map.items():

            # check if going backwards
            if offset[0] and offset[0] == prev_offset[0] * -1:
                continue
            if offset[1] and offset[1] == prev_offset[1] * -1:
                continue

            # check new direction is in bounds
            new_location = (location[0] + offset[0],
                            location[1] + offset[1])
            if not 0 <= new_location[0] <= x_max:
                continue
            if not 0 <= new_location[1] <= y_max:
                continue

            # check length if direction is straight
            if prev_offset == offset:
                new_length = length + 1
                if length_max and new_length > length_max:
                    continue
            else:
                if length and length_min and length < length_min:
                    continue
                new_length = 1

            # check new heat loss (aka distance)
            new_heat_loss = heat_loss + \
                int(map_data[new_location[1]][new_location[0]])
            if new_heat_loss >= heat_loss_map[new_location[1]][new_location[0]][(direction, offset, new_length)]:  # noqa: E501
                continue
            heat_loss_map[new_location[1]][new_location[0]][(direction, offset, new_length)] = new_heat_loss  # noqa: E501
            heappush(queue, [new_heat_loss, new_location, offset, new_length])


def process_map(input):
    data = []
    for line in input.split('\n'):
        data.append([*line])
    return data


def main():

    # script args
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 17")
    parser.add_argument("filename", help="File containing the puzzle input")
    args = parser.parse_args()

    # process puzzle input
    with open(args.filename) as file:
        puzzle_input = file.read()
    map_data = process_map(puzzle_input)
    # calculate answer for part 1
    answer1 = dijsktra(map_data, length_max=3)
    print("Answer for Part 1:", answer1)

    # calculate answer for part 2
    answer2 = dijsktra(map_data, length_min=4, length_max=10)
    print("Answer for Part 2:", answer2)


if __name__ == "__main__":
    main()
