#!/usr/bin/env python3
from dataclasses import dataclass
import numpy as np
import pathlib
from typing import TypeAlias

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "06.txt"

Grid: TypeAlias = np.ndarray


@dataclass
class Coordinate:
    x: int
    y: int


def parse_coor(inp: str):
    coordinates: list[str] = inp.split(",")
    return Coordinate(int(coordinates[0]), int(coordinates[1]))


def turn_on(c1: Coordinate, c2: Coordinate, grid: Grid) -> Grid:
    min_x: int = min(c1.x, c2.x)
    max_x: int = max(c1.x, c2.x)
    min_y: int = min(c1.y, c2.y)
    max_y: int = max(c1.y, c2.y)

    grid[min_y : max_y + 1, min_x : max_x + 1] = 1

    return grid


def turn_off(c1: Coordinate, c2: Coordinate, grid: Grid) -> Grid:
    min_x: int = min(c1.x, c2.x)
    max_x: int = max(c1.x, c2.x)
    min_y: int = min(c1.y, c2.y)
    max_y: int = max(c1.y, c2.y)

    grid[min_y : max_y + 1, min_x : max_x + 1] = 0

    return grid


def toggle(c1: Coordinate, c2: Coordinate, grid: Grid) -> Grid:
    min_x: int = min(c1.x, c2.x)
    max_x: int = max(c1.x, c2.x)
    min_y: int = min(c1.y, c2.y)
    max_y: int = max(c1.y, c2.y)

    grid[min_y : max_y + 1, min_x : max_x + 1] = (
        1 - grid[min_y : max_y + 1, min_x : max_x + 1]
    )

    return grid


def parse_instruction(instr: str, grid: Grid) -> Grid:
    words: list[str] = instr.split()
    if words[0] == "turn" and words[1] == "on":
        return turn_on(parse_coor(words[2]), parse_coor(words[4]), grid)

    if words[0] == "turn" and words[1] == "off":
        return turn_off(parse_coor(words[2]), parse_coor(words[4]), grid)

    if words[0] == "toggle":
        return toggle(parse_coor(words[1]), parse_coor(words[3]), grid)

    raise ValueError("Improperly parsed instruction!")


def main() -> None:
    grid: np.ndarray = np.zeros((1000, 1000))

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            grid = parse_instruction(line, grid)

    # Count lights on
    print(np.count_nonzero(grid == 1))


if __name__ == "__main__":
    main()
