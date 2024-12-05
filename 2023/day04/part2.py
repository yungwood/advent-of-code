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


# return an array with the winning numbers
def get_winning_numbers(input):
    winners = []
    for number in input["numbers"]:
        if number in input["winners"]:
            winners.append(number)
    return winners


# process puzzle input file
with open(args.filename) as file:

    winning_numbers = {}
    card_count = {}
    for i, line in enumerate(file):
        # parse card data
        parsed = parse_card_data(line)
        # get count of winning numbers
        winning_numbers[i] = len(get_winning_numbers(parsed))
        # make sure we add a count for the card we get
        if i not in card_count:
            card_count[i] = 1
        else:
            card_count[i] += 1
        # add additional cards won
        for j in range(i + 1, i + winning_numbers[i] + 1):
            if j not in card_count:
                card_count[j] = card_count[i]
            else:
                card_count[j] += card_count[i]

    # sum all values
    sum = 0
    for key in card_count:
        sum += card_count[key]

    # print answer
    print("The answer is {}!".format(sum))
