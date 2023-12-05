import argparse
import logging
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
try:
    args = parser.parse_args()
except:
    print("Try using the -h option for more info")
    exit(0)

# return an array with the seeds
def get_seeds(input):
    results = re.search(r"seeds: ((?:\d|\s)+)", input)
    results = re.findall(r"(\d+ \d+)", results.group(0))
    seeds = []
    for result in results:
        numbers = [int(i) for i in result.split(" ")]
        seeds.append([numbers[0], numbers[0] + numbers[1] - 1])
    return seeds

# parse a map
def get_map(input, name):
    results = re.search(r"{} map:\n((?:(?:\d| )+\n?)+)".format(name), input)
    map = []
    for line in results.group(1).strip("\n").split("\n"):
        numbers = [int(i) for i in re.findall(r"(\d+)", line)]
        map.append(numbers)
    return map

# use a parsed map to convert a value, also return the remaining offset so those records can be skipped
def process_map(maps, seed, skip=1):
    for map in maps:
        if seed >= map[1] and seed < (map[1] + map[2]):
            offset = seed - map[1]
            remaining_offset = map[2] - offset
            new_value = map[0] + offset
            return [new_value, remaining_offset]
    return [seed, skip]

# parse value through all maps from start to finish
# remember the smallest remaining offset from all conversions and return
def seed_to_location(map_data, seed):
    location = [seed, 1]
    skippable = 0
    for map_name in map_data.keys():
        location = process_map(map_data[map_name], location[0], location[1])
        if not skippable or location[1] < skippable:
            skippable = location[1]
    return [location[0], skippable]

# process puzzle input file
with open(args.filename) as file:

    input = file.read()
        
    seeds = get_seeds(input)

    map_names = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

    map_data = {}
    for i in range(0, len(map_names) - 1):
        map_name = "{}-to-{}".format(map_names[i], map_names[i+1])
        map_data[map_name] = get_map(input, map_name)

    smallest = 0
    # calculate seeds to find smallest
    for seed in seeds:
        i = seed[0]
        while i <= seed[1]:
            value = seed_to_location(map_data, i)
            if not smallest or value[0] < smallest:
                smallest = value[0]
            # skip over the remaining map offset (as all remaining values will increment by 1)
            i += value[1]

    # # print answer
    print("The answer is {}!".format(smallest))
