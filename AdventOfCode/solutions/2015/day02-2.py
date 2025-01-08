import unittest
from util.input import run_with_input_lines
import sys

from dataclasses import dataclass


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


def solve(input: list[str]) -> int:
    total_needed: int = 0

    for line in input:
        line: str = line.strip()  # remove newline character at the end

        d: Dimension = parse_line(line)

        total_needed += smallest_perimeter(d)
        total_needed += multiply_all_sides(d)

    return total_needed


class TestSolve(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve(["2x3x4"]), 34)

    def test_example2(self):
        self.assertEqual(solve(["1x1x10"]), 14)


def run() -> None:
    run_with_input_lines(2015, 2, 2, sys.modules[__name__])
