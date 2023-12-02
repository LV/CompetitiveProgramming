from dataclasses import dataclass
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "02.txt"

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


def get_power(g: Game) -> int:
    red: int = 0
    green: int = 0
    blue: int = 0
    for s in g.sets:
        if s.red > red:
            red = s.red
        if s.green > green:
            green = s.green
        if s.blue > blue:
            blue = s.blue

    return red * green * blue


def main() -> None:
    total: int = 0

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            total += get_power(parse_line(line))

    print(total)


if __name__ == "__main__":
    main()
