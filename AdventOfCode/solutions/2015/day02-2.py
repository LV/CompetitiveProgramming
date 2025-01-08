#!/usr/bin/env python3
from dataclasses import dataclass
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "02.txt"


@dataclass
class Dimension:
    l: int
    w: int
    h: int


def smallest_perimeter(d: Dimension) -> int:
    # Get areas of all different sides
    areas: list[int] = [d.l * d.w, d.w * d.h, d.h * d.l]

    # Get the index of the smallest area from the sides
    index: int = areas.index(min(areas))

    # Get the perimeter using the index as a reference of which side to pull from
    return [(d.l * 2) + (d.w * 2), (d.w * 2) + (d.h * 2), (d.h * 2) + (d.l * 2)][index]


def multiply_all_sides(d: Dimension) -> int:
    return d.l * d.w * d.h


def parse_line(line: str) -> Dimension:
    tupl = line.split("x")
    return Dimension(l=int(tupl[0]), w=int(tupl[1]), h=int(tupl[2]))


def main() -> None:
    total_needed: int = 0

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end

            d: Dimension = parse_line(line)

            total_needed += smallest_perimeter(d)
            total_needed += multiply_all_sides(d)

    print(total_needed)


if __name__ == "__main__":
    main()
