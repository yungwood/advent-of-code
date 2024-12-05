import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# use regex to get card id & card data
def parse_card_data(input):
    # split card id and card data
    parsed = re.search(r"Card\s+(\d+): (.+)", input)
    data = parsed.group(2).split("|")
    result = {
        "winners": [],
        "numbers": []
    }
    for winner in re.findall(r"\d+", data[0]):
        result["winners"].append(int(winner))
    for number in re.findall(r"\d+", data[1]):
        result["numbers"].append(int(number))
    return result


# check for winning numbers
def get_winning_numbers(input):
    winners = []
    for number in input["numbers"]:
        if number in input["winners"]:
            winners.append(number)
    return winners


# process puzzle input file
with open(args.filename) as file:

    sum = 0
    for line in file:
        # parse card data
        parsed = parse_card_data(line)
        # check how many winning numbers
        winners = get_winning_numbers(parsed)
        if len(winners):
            sum += 2 ** (len(winners) - 1)

    # print answer
    print("The answer is {}!".format(sum))
