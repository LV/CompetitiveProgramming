#!/usr/bin/env python3
from dataclasses import dataclass
from sortedcontainers import SortedDict  # requires `pip install sortedcontainers`
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "03.txt"
f = open(file_path, "r")


# `frozen` makes it so that each Coordinate is immutable
# `order` makes it so that Coordinate is comparable based on its fields
#   making it orderable for the SortedDict
@dataclass(frozen=True, order=True)
class Coordinate:
    x: int
    y: int


def main() -> None:
    x: int = 0
    y: int = 0

    houses: SortedDict[Coordinate] = SortedDict()

    # Make the initial house contain a present
    houses[Coordinate(0, 0)] = 1

    for char in f.read():
        match char:
            case "^":
                y += 1
            case "v":
                y -= 1
            case "<":
                x -= 1
            case ">":
                x += 1
            case _:
                break

        current_coordinate: Coordinate = Coordinate(x, y)

        if current_coordinate in houses:
            houses[current_coordinate] += 1
        else:
            houses[current_coordinate] = 1

    print(len(houses))


if __name__ == "__main__":
    main()
