import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# return array of values based on label from input data
def parse_line(input, label):
    results = re.search(r"{}: ((?:\d|\s)+)".format(label), input)
    return [int(''.join(re.findall(r"(\d+)", results.group(0))))]


# return an array of arrays with the race data
def parse_races(input):
    times = parse_line(input, "Time")
    distances = parse_line(input, "Distance")
    return list(zip(times, distances))


# calculate distance travelled given total time and button time
def calculate_distance(total_time, button_time):
    movement_time = total_time - button_time
    speed = button_time
    return movement_time * speed


# process puzzle input file
with open(args.filename) as file:

    input = file.read()

    race_data = parse_races(input)

    better_races = {}
    for race in race_data:
        better_races[race[0]] = []
        for i in range(1, race[0]):
            distance = calculate_distance(race[0], i)
            if distance > race[1]:
                better_races[race[0]].append([distance, i])

    product = 1
    for key in better_races.keys():
        product = product * len(better_races[key])

    # print answer
    print("The answer is {}!".format(product))
