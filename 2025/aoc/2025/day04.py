import sys
from dataclasses import dataclass


@dataclass
class ParsedInput:
    grid: list[list[str]]

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    def get_accessible_rolls(self, update: bool = False) -> int:
        accessible_rolls = 0
        for x in range(0, self.height):
            for y in range(0, self.width):
                value = self.get_value(x, y)
                if not value == "@":
                    continue
                neighbor_values = self.get_neighbor_values(x, y)
                if neighbor_values.count("@") >= 4:
                    continue
                accessible_rolls += 1
                if update:
                    self.set_value(x, y, "x")
        return accessible_rolls

    def get_neighbor_values(self, row: int, col: int) -> list[str]:
        values: list[str] = []
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if row_offset == 0 and col_offset == 0:
                    continue
                x = row + row_offset
                y = col + col_offset
                if x < 0 or x >= self.height:
                    values.append("")
                    continue
                if y < 0 or y >= self.width:
                    values.append("")
                    continue
                values.append(self.grid[x][y])
        return values

    def get_value(self, row: int, col: int) -> str:
        return self.grid[row][col]

    def set_value(self, row: int, col: int, value: str):
        self.grid[row][col] = value


def parse(raw: str) -> ParsedInput:
    puzzle_input = raw.splitlines()
    parsed = ParsedInput([list(line) for line in puzzle_input])
    return parsed


def part1(data: ParsedInput) -> int:
    return data.get_accessible_rolls()


def part2(data: ParsedInput) -> int:
    accessible_rolls = None
    moved = 0
    while accessible_rolls != 0:
        accessible_rolls = data.get_accessible_rolls(True)
        moved += accessible_rolls
    return moved


if __name__ == "__main__":
    raw = sys.stdin.read()
    if not raw:
        print("No input received on stdin.")
        sys.exit(1)

    data = parse(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
