#!/usr/bin/env python3
from dataclasses import dataclass
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "02.txt"


@dataclass
class Dimension:
    l: int
    w: int
    h: int


def surface_area(d: Dimension) -> int:
    return (2 * d.l * d.w) + (2 * d.w * d.h) + (2 * d.h * d.l)


def smallest_area(d: Dimension) -> int:
    return min([d.l * d.w, d.w * d.h, d.h * d.l])


def parse_line(line: str) -> Dimension:
    tupl = line.split("x")
    return Dimension(l=int(tupl[0]), w=int(tupl[1]), h=int(tupl[2]))


def main() -> None:
    total_needed: int = 0

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end

            d: Dimension = parse_line(line)

            total_needed += surface_area(d)
            total_needed += smallest_area(d)

    print(total_needed)


if __name__ == "__main__":
    main()
