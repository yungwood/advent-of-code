import argparse
import re
from math import lcm

# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# process direction data
def get_directions(input):
    results = re.search(r"([LR]+)", input)
    return list(map(lambda x: 0 if x == "L" else 1, [*results.group(0)]))


# process location data
def get_locations(input):
    data = {}
    pattern = r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)"
    results = re.findall(pattern, input)
    for result in results:
        data[result[0]] = [result[1], result[2]]
    return data


# calculate steps for a ghost loop
def calc_ghost_loop(start_location, direction_data):
    count = 0
    current_location = start_location
    while not current_location.endswith('Z'):
        # add current location to start_locations
        for direction in direction_data:
            count += 1
            current_location = location_data[current_location][direction]
    return count


# process puzzle input file
with open(args.filename) as file:
    input = file.read()

direction_data = get_directions(input)
location_data = get_locations(input)

# calculate ghost loops
loop_sizes = []
start_locations = [key for key in location_data.keys() if key.endswith('A')]
for start_location in start_locations:
    loop_sizes.append(calc_ghost_loop(start_location, direction_data))
print("The answer is {}!".format(lcm(*loop_sizes)))
