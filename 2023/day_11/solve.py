import argparse


# parse script args
parser = argparse.ArgumentParser(description='Advent of Code 2023: Day 11')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# parse map data to list of lists
def parse_map(input):
    map_data = []
    for line in input.split('\n'):
        map_data.append(list(line.strip()))
    return map_data


# expand universe
def get_empty_universe_planes(map_data):
    # find columns without galaxies
    x_empty = []
    for x in range(len(map_data[0])):
        column_data = [row[x] for row in map_data]
        if '#' not in column_data:
            x_empty.append(x)
    # find rows without galaxies
    y_empty = []
    for y, data in enumerate(map_data):
        if '#' not in data:
            y_empty.append(y)
    return [x_empty, y_empty]


# get galaxy locations
def get_galaxy_locations(map_data, min_empty_space=1):
    locations = []
    y = 0
    while y < len(map_data):
        if "#" not in map_data[y]:
            y += min_empty_space
            continue
        locations.extend([[x, y] for x, val in enumerate(map_data[y])
                          if val == "#"])
        y += 1
    return locations


# re-calculate galaxy locations with expansion
def get_expanded_galaxy_locations(galaxy_locations, empty_planes, size):
    new_locations = []
    for galaxy in galaxy_locations:
        x_empty = len(list(filter(lambda z: (z < galaxy[0]), empty_planes[0])))
        y_empty = len(list(filter(lambda z: (z < galaxy[1]), empty_planes[1])))
        new_locations.append([galaxy[0] + (x_empty * size),
                              galaxy[1] + (y_empty * size)])
    return new_locations


# calculate distance between 2 given locations
def calculate_distance(location1, location2):
    x = abs(location1[0] - location2[0])
    y = abs(location1[1] - location2[1])
    return x + y


# process puzzle input file
with open(args.filename) as file:
    input = file.read()

# parse map / galaxies
map_data = parse_map(input)
empty_planes = get_empty_universe_planes(map_data)
galaxy_locations = get_galaxy_locations(map_data)

# calculate part 1
galaxy_locations_part1 = get_expanded_galaxy_locations(galaxy_locations,
                                                       empty_planes, 1)
distances_part1 = []
for i, galaxy in enumerate(galaxy_locations_part1):
    for j in range(i, len(galaxy_locations_part1)):
        if i == j:
            continue
        distances_part1.append(calculate_distance(galaxy,
                                                  galaxy_locations_part1[j]))
answer = sum(distances_part1)
print("The answer for part 1 is {}".format(answer))

# calculate part 2
galaxy_locations_part2 = get_expanded_galaxy_locations(galaxy_locations,
                                                       empty_planes, 1000000)
distances_part2 = []
for i, galaxy in enumerate(galaxy_locations_part2):
    for j in range(i, len(galaxy_locations_part2)):
        if i == j:
            continue
        distances_part2.append(calculate_distance(galaxy,
                                                  galaxy_locations_part2[j]))
answer = sum(distances_part2)
print("The answer for part 2 is {}".format(answer))
