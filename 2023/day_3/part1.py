import argparse
import re


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# return an array with location of each symbol on a line
def get_symbols(input):
    # find all symbols
    results = re.finditer(r"([^\d\.])", input)
    # save location of symbols to array
    symbols = []
    for match in results:
        symbols.append(match.start())
    return symbols


# return a dict with each number match as key and span for value
def get_numbers(input):
    # find all numbers
    results = re.finditer(r"(\d+)", input)
    # save location of symbols to array
    numbers = []
    for match in results:
        numbers.append([match.group(), match.span()])
    return numbers


# check if a number is located near a symbol
def check_symbol_adjacent(symbols_map, line_no, span):
    # test line before number
    if line_no > 0:
        for symbol_position in symbols_map[(line_no - 1)]:
            if symbol_position >= span[0] - 1 and symbol_position <= span[1]:
                return True

    # test same line where number is located
    for symbol_position in symbols_map[line_no]:
        # if symbol is left of the number
        if symbol_position == span[0] - 1:
            return True
        # if symbol is right of the number
        if symbol_position == span[1]:
            return True

    # test line after number
    if line_no < len(symbols_map) - 1:
        for symbol_position in symbols_map[(line_no + 1)]:
            if symbol_position >= span[0] - 1 and symbol_position <= span[1]:
                return True

    return False


# process puzzle input file
with open(args.filename) as file:

    # create a dict with every line and location of symbols
    symbols_map = {}
    # create a dict with every line and numbers/spans
    numbers_map = {}
    for line_count, line in enumerate(file):
        symbols_map[line_count] = get_symbols(line.rstrip('\n'))
        numbers_map[line_count] = get_numbers(line.rstrip('\n'))

    sum = 0

    # loop through each number found and test to see if located near symbol
    for line_no, number_matches in numbers_map.items():
        for match in number_matches:
            if check_symbol_adjacent(symbols_map, line_no, match[1]):
                sum += int(match[0])

    # print answer
    print("The answer is {}!".format(sum))
