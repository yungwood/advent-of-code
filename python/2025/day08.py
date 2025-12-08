import math
import sys

Location = tuple[int, int, int]
ParsedInput = list[Location]


def parse(raw: str) -> ParsedInput:
    boxes = []
    for line in raw.splitlines():
        boxes.append(Location(int(i) for i in line.split(",")))
    return ParsedInput(boxes)


def part1(data: ParsedInput) -> int:
    max_connections = 1000 if len(data) > 20 else 10
    distances = calculate_all_distances(data)
    connections = list(distances.keys())[:max_connections]
    circuits = get_circuits(connections)
    circuit_sizes = [len(i) for i in circuits]
    return math.prod(circuit_sizes[:3])


def part2(data: ParsedInput) -> int:
    distances = calculate_all_distances(data)
    nodes = []
    for a, b in distances:
        if a not in nodes:
            nodes.append(a)
        if b not in nodes:
            nodes.append(b)
        if len(nodes) == len(data):
            return data[a][0] * data[b][0]
    raise Exception("Got to end of distances list without connecting all nodes!")


def get_circuits(connections: list[tuple[int, int]]) -> list:
    circuits = []
    for a, b in connections:
        new_circuit = {a, b}
        merged = []
        for circuit in circuits:
            if circuit & new_circuit:
                new_circuit |= circuit
            else:
                merged.append(circuit)
        merged.append(new_circuit)
        circuits = merged
    return sorted(circuits, key=len, reverse=True)


def calculate_all_distances(boxes: list[Location]) -> dict:
    distances = {}
    n = len(boxes)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            elif j > i:
                if not (i, j) in distances:
                    distances[i, j] = calculate_distance(boxes[i], boxes[j])
            elif i > j:
                if not (j, i) in distances:
                    distances[j, i] = calculate_distance(boxes[i], boxes[j])
    return dict(sorted(distances.items(), key=lambda item: item[1]))


def calculate_distance(a: Location, b: Location) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
