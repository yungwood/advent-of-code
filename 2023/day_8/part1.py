import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# process direction data
def get_directions(input):
    results = re.search(r"([LR]+)", input)
    return [*results.group(0)]


# process location data
def get_locations(input):
    data = {}
    results = re.findall(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", input)
    for result in results:
        data[result[0]] = [result[1], result[2]]
    return data


# process puzzle input file
with open(args.filename) as file:
    input = file.read()
direction_data = get_directions(input)
location_data = get_locations(input)

# calculate path, starting at 'AAA'
current_location = 'AAA'
steps = 0
while current_location != 'ZZZ':
    for direction in direction_data:
        if direction == 'L':
            current_location = location_data[current_location][0]
        else:
            current_location = location_data[current_location][1]
        steps += 1
        if current_location == 'ZZZ':
            break

print("The answer is {}!".format(steps))
