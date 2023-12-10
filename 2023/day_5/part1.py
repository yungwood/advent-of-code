import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# return an array with the seeds
def get_seeds(input):
    results = re.search(r"seeds: ((?:\d|\s)+)", input)
    results = re.findall(r"(\d+)", results.group(0))
    seeds = []
    for result in results:
        seeds.append(int(result))
    return seeds


# process a map
def get_map(input, name):
    results = re.search(r"{} map:\n((?:(?:\d| )+\n?)+)".format(name), input)
    map = []
    for line in results.group(1).strip("\n").split("\n"):
        numbers = [int(i) for i in re.findall(r"(\d+)", line)]
        map.append(numbers)
    return map


def process_map(maps, seed):
    for map in maps:
        if seed >= map[1] and seed < (map[1] + map[2]):
            offset = seed - map[1]
            new_value = map[0] + offset
            return new_value
    return seed


def seed_to_location(map_data, seed):
    location = seed
    for map_name in map_data.keys():
        location = process_map(map_data[map_name], location)
    return location


# process puzzle input file
with open(args.filename) as file:

    input = file.read()

    seeds = get_seeds(input)

    map_names = ["seed", "soil", "fertilizer", "water", "light", "temperature",
                 "humidity", "location"]

    map_data = {}
    for i in range(0, len(map_names) - 1):
        map_name = "{}-to-{}".format(map_names[i], map_names[i+1])
        map_data[map_name] = get_map(input, map_name)

    # calculate seed locations
    seed_locations = {}
    for seed in seeds:
        seed_locations[seed] = seed_to_location(map_data, seed)

    # find smallest
    smallest = 0
    for key, value in seed_locations.items():
        if not smallest:
            smallest = value
        if value < smallest:
            smallest = value

    # print answer
    print("The answer is {}!".format(smallest))
