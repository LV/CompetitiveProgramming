#!/usr/bin/env python3
from dataclasses import dataclass
from sortedcontainers import SortedDict  # requires `pip install sortedcontainers`
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "03.txt"
f = open(file_path, "r")


# `frozen` makes it so that each Coordinate is immutable
# `order` makes it so that Coordinate is comparable based on its fields
#   making it orderable for the SortedDict
@dataclass(frozen=True, order=True)
class Coordinate:
    x: int
    y: int


def main() -> None:
    x_santa: int = 0
    y_santa: int = 0
    x_robo: int = 0
    y_robo: int = 0

    count: int = 0

    houses: SortedDict[Coordinate] = SortedDict()

    # Make the initial house contain two presents
    houses[Coordinate(0, 0)] = 2

    for char in f.read():
        if count % 2 == 0:
            match char:
                case "^":
                    y_santa += 1
                case "v":
                    y_santa -= 1
                case "<":
                    x_santa -= 1
                case ">":
                    x_santa += 1
                case _:
                    break
        else:
            match char:
                case "^":
                    y_robo += 1
                case "v":
                    y_robo -= 1
                case "<":
                    x_robo -= 1
                case ">":
                    x_robo += 1
                case _:
                    break

        if count % 2 == 0:
            current_coordinate: Coordinate = Coordinate(x_santa, y_santa)
        else:
            current_coordinate: Coordinate = Coordinate(x_robo, y_robo)

        if current_coordinate in houses:
            houses[current_coordinate] += 1
        else:
            houses[current_coordinate] = 1

        count += 1

    print(len(houses))


if __name__ == "__main__":
    main()
