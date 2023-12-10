import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# use regex to get first & last number, join them and return as int
def get_calibration_value(input):
    # find numbers, incl as words
    # had to add positive lookahead to deal with overlapping number words
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    numbers = re.findall(pattern, input)
    # replace first/last match with number if word
    number_map = ["one", "two", "three", "four", "five", "six", "seven",
                  "eight", "nine"]
    if numbers[0] in number_map:
        numbers[0] = number_map.index(numbers[0])+1
    if numbers[-1] in number_map:
        numbers[-1] = number_map.index(numbers[-1])+1
    # join first/last result and convert to int
    calibration_value = int("{}{}".format(numbers[0], numbers[-1]))
    return calibration_value


# process puzzle input
with open(args.filename) as file:
    calibration_values = []
    for line in file:
        calibration_values.append(get_calibration_value(line.rstrip('\n')))
    # sum values
    sum = 0
    for value in calibration_values:
        sum += value
    # print answer
    print("The answer is {}!".format(sum))
