import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# use regex to get game id & game data
def parse_game_data(input):
    # split game id and game data
    parsed = re.search(r"Game (\d+): (.+)", input)
    id = int(parsed.group(1))
    data = parsed.group(2)
    # split data into games
    games = data.split("; ")
    # get highest of each colour from all games
    result = {
        "blue": 0,
        "green": 0,
        "red": 0
    }
    for game in games:
        items = game.split(", ")
        for item in items:
            parsed = re.search(r"(\d+) (blue|green|red)", item)
            colour = parsed.group(2)
            count = int(parsed.group(1))
            if count > result[colour]:
                result[colour] = count
    return [id, result]


# use regex to get first & last number, join them and return as int
def get_calibration_value(input):
    # find all digits
    numbers = re.findall(r"\d", input)
    # join first/last result and convert to int
    calibration_value = int("{}{}".format(numbers[0], numbers[-1]))
    return calibration_value


# process puzzle input file
with open(args.filename) as file:

    # get values
    sum = 0
    for line in file:
        parsed = parse_game_data(line)
        id = parsed[0]
        results = parsed[1]
        if results['blue'] > 14:
            continue
        if results['green'] > 13:
            continue
        if results['red'] > 12:
            continue
        sum += parsed[0]

    # print answer
    print("The answer is {}!".format(sum))
