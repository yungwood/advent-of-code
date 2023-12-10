import argparse
import logging
import re

# basic logging config
# example: YYYY-MM-DD HH:MM:SS [ThreadName] (function) LEVEL: essage
logging.basicConfig(
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger()

# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
parser.add_argument('--debug', action='store_true',
                    help='Increase logging verbosity')
args = parser.parse_args()

# enable debug logging
if args.debug:
    log.setLevel(logging.DEBUG)


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


# use a parsed map to convert a value
# also return the remaining offset so those records can be skipped
def process_map(maps, seed):
    range_starts = []
    for map in maps:
        if seed <= map[1]:
            range_starts.append(map[1])
        if seed >= map[1] and seed < (map[1] + map[2]):
            offset = seed - map[1]
            remaining_offset = map[2] - offset
            new_value = map[0] + offset
            log.debug("{} becomes {} ({} to end of array)".
                      format(seed, new_value, remaining_offset))
            return [new_value, remaining_offset]
    # if there is no array that starts after this seed then return 0 for offset
    if not range_starts:
        range_starts = [0]
    log.debug("{} remains {} ({} to start of next array)"
              .format(seed, seed, min(range_starts)))
    return [seed, min(range_starts)]


# parse value through all maps from start to finish
# remember the smallest remaining offset from all conversions and return
def seed_to_location(map_data, seed):
    location = [seed, 1]
    skippable = None
    for map_name in map_data.keys():
        location = process_map(map_data[map_name], location[0])
        if not skippable or location[1] < skippable and location[1]:
            skippable = location[1]
    log.debug("* Seed {} = Location {}, skippable={}"
              .format(seed, location[1], skippable))
    return [location[0], skippable]


# process puzzle input file
with open(args.filename) as file:

    input = file.read()

    log.debug("Parsing seed ranges")
    seeds = get_seeds(input)
    log.debug("seeds = {}".format(seeds))

    log.debug("Parsing map data")
    map_names = ["seed", "soil", "fertilizer", "water", "light", "temperature",
                 "humidity", "location"]
    map_data = {}
    for i in range(0, len(map_names) - 1):
        map_name = "{}-to-{}".format(map_names[i], map_names[i+1])
        map_data[map_name] = get_map(input, map_name)
        log.debug("{} = {}".format(map_name, map_data[map_name]))

    log.debug("Calculate seeds to find smallest location value")
    smallest = 0
    # calculate seeds to find smallest
    for seed in seeds:
        log.debug("*** Calculate seeds {} to {}".format(seed[0], seed[1]))
        i = seed[0]
        while i <= seed[1]:
            log.debug("** Calculate seed {}".format(i))
            value = seed_to_location(map_data, i)
            if not smallest or value[0] < smallest:
                log.debug("{} is now the smallest location value!"
                          .format(value[0]))
                smallest = value[0]
            # skip over the remaining map offset
            # (as all remaining values will increment by 1)
            log.debug("Skip forward {} seed(s)".format(value[1]))
            i += value[1]

    # print answer
    log.info("The smallest location value is {}!".format(smallest))
