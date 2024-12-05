import argparse


# parse script args
parser = argparse.ArgumentParser(description='advent of code')
parser.add_argument('filename', help='The file containing the puzzle input')
args = parser.parse_args()


# calculate funnel values
def calculate_funnel(input):
    data = [input]
    while not all(value == 0 for value in data[-1]):
        data.append([])
        for i in range(len(data[-2]) - 1):
            data[-1].append(data[-2][i + 1] - data[-2][i])
    return data


# calculate next funnel value
def calculate_next_funnel_value(funnel):
    data = funnel
    data[-1].append(0)
    for depth in reversed(range(len(data) - 1)):
        data[depth].append(data[depth][-1] + data[depth + 1][-1])
    return data


# process puzzle input file
with open(args.filename) as file:
    input = file.read()

# parse puzzles
data = []
for line in input.split('\n'):
    data.append([int(value) for value in line.strip().split(' ')])

# calc answer
answer = 0
for item in data:
    funnel = calculate_funnel(item)
    funnel = calculate_next_funnel_value(funnel)
    answer += funnel[0][-1]

print("The answer is {}!".format(answer))
