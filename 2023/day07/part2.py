import argparse


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# get card counts and determine type of hand
def get_hand_type(hand):
    card_counts = []
    joker_count = 0
    for card in set(list(hand)):
        # if card is joker, save count for afterwards
        if card == "J":
            joker_count = list(hand).count(card)
            continue
        card_counts.append(list(hand).count(card))
    card_counts.sort(reverse=True)
    # if hand contains jokers, add jokers to greatest count
    if joker_count:
        # cater for 'JJJJJ' in puzzle_input
        if card_counts:
            card_counts[0] += joker_count
        else:
            card_counts.append(joker_count)
    # work out hand type
    match len(card_counts):
        case 1:
            # 5 of a kind
            return 6
        case 2:
            if card_counts[0] == 4:
                # 4 of a kind
                return 5
            if card_counts[0] == 3:
                # full house
                return 4
        case 3:
            if card_counts[0] == 3:
                # 3 of a kind
                return 3
            if card_counts[0] == 2:
                # two pair
                return 2
        case 4:
            # one pair
            return 1
        case 5:
            # highest card
            return 0


# return a list with parsed game info
def parse_game(input):
    result = input.split(" ")
    result.append(get_hand_type(result[0]))
    result[1] = int(result[1])
    cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    for card in result[0]:
        result.append(cards.index(card))
    return result


# process puzzle input file
with open(args.filename) as file:
    games = []
    for line in file:
        games.append(parse_game(line.strip("\n")))

    # sort all games from worst to best by hand_type then cards
    games.sort(key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))

    # calculate answer
    sum = 0
    for rank, game in enumerate(games, start=1):
        sum += game[1] * rank

    print("The answer is {}!".format(sum))
