import argparse


def trace_rays(map_data, start_location, start_step):
    seen = set()
    illuminated = set()
    queue = [(start_location, start_step)]
    while queue:

        # pop item off queue, make sure it's new
        ray = queue.pop(0)
        if ray in seen:
            continue
        location = ray[0]

        # check if location is within bounds
        if not 0 <= location[0] < len(map_data[0]):
            continue
        if not 0 <= location[1] < len(map_data):
            continue

        # add to seen list
        seen.add(ray)

        # get char at location and step
        char = map_data[location[1]][location[0]]
        step = ray[1]

        # add current location to illuminated tiles
        illuminated.add(location)

        # process char
        if char == "-" and step[1]:
            new_location = (location[0] + 1, location[1])
            queue.append((new_location, (1, 0)))
            new_location = (location[0] - 1, location[1])
            queue.append((new_location, (-1, 0)))
            continue
        if char == "|" and step[0]:
            new_location = (location[0], location[1] - 1)
            queue.append((new_location, (0, -1)))
            new_location = (location[0], location[1] + 1)
            queue.append((new_location, (0, 1)))
            continue
        if char == "\\":
            new_step = (step[1], step[0])
            new_location = (location[0] + new_step[0],
                            location[1] + new_step[1])
            queue.append((new_location, new_step))
            continue
        if char == "/":
            new_step = (step[1] * -1, step[0] * -1)
            new_location = (location[0] + new_step[0],
                            location[1] + new_step[1])
            queue.append((new_location, new_step))
            continue

        # must be continuing in same direction
        new_location = (location[0] + step[0], location[1] + step[1])
        queue.append((new_location, step))

    return len(illuminated)


def process_map(input):
    data = []
    for line in input.split('\n'):
        data.append(tuple([*line]))
    return tuple(data)


def main():

    # script args
    parser = argparse.ArgumentParser(description="Advent of Code 2023: Day 16")
    parser.add_argument("filename", help="File containing the puzzle input")
    args = parser.parse_args()

    # process puzzle input
    with open(args.filename) as file:
        puzzle_input = file.read()
    map_data = process_map(puzzle_input)

    # calculate answer for part 1
    answer1 = trace_rays(map_data, (0, 0), (1, 0))
    print("Answer for Part 1:", answer1)

    # calculate answer for part 2
    illuminated_counts = []
    # top row
    for x in range(0, len(map_data[0]) + 1):
        illuminated_counts.append(trace_rays(map_data, (x, 0), (0, 1)))
        illuminated_counts.append(trace_rays(map_data,
                                             (x, len(map_data) - 1),
                                             (0, -1)))
    for y in range(0, len(map_data) + 1):
        illuminated_counts.append(trace_rays(map_data, (0, y), (1, 0)))
        illuminated_counts.append(trace_rays(map_data,
                                             (len(map_data[0]) - 1, y),
                                             (-1, 0)))
    answer2 = max(illuminated_counts)
    print("Answer for Part 2:", answer2)


if __name__ == "__main__":
    main()
