from dataclasses import dataclass
import pathlib

test_file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "02-t.txt"
input_file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "02-i.txt"


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class GameSet:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    game_id: int
    sets: list[GameSet]


def parse_set(s: str) -> GameSet:
    colors: list[str] = s.split(",")
    red: int = 0
    green: int = 0
    blue: int = 0
    for c in colors:
        num, col = c.split()
        if col == "red":
            red = int(num)
        if col == "green":
            green = int(num)
        if col == "blue":
            blue = int(num)
    return GameSet(red=red, green=green, blue=blue)


def parse_sets(sets: list[str]) -> list[GameSet]:
    return [parse_set(s) for s in sets]


def parse_line(line: str) -> Game:
    # Get Game ID:
    colon_pos: int = line.find(":")
    game_id: int = int(line[5:colon_pos])
    sets_to_parse: list[str] = line[colon_pos + 1 :].split(";")
    return Game(game_id=game_id, sets=parse_sets(sets_to_parse))


def filter_valid(g: Game) -> int:
    for s in g.sets:
        if s.red > MAX_RED or s.green > MAX_GREEN or s.blue > MAX_BLUE:
            return 0
    return g.game_id


def solve(inp: pathlib.Path) -> int:
    total: int = 0

    with open(inp, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            total += filter_valid(parse_line(line))

    return total


def main() -> None:
    assert solve(test_file_path) == 8
    print(solve(input_file_path))


if __name__ == "__main__":
    main()
