import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# use regex to get first & last number, join them and return as int
def get_calibration_value(input):
    # find all digits
    numbers = re.findall(r"\d", input)
    # join first/last result and convert to int
    calibration_value = int("{}{}".format(numbers[0], numbers[-1]))
    return calibration_value


# process puzzle input file
with open(args.filename) as file:

    # get calibration values
    calibration_values = []
    for line in file:
        calibration_values.append(get_calibration_value(line.rstrip('\n')))

    # sum calibration values
    sum = 0
    for value in calibration_values:
        sum += value

    # print answer
    print("The answer is {}!".format(sum))
