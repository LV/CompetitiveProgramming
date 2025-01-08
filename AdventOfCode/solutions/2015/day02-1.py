import unittest
from util.input import run_with_input_lines
import sys

from dataclasses import dataclass


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


def solve(input: list[str]) -> int:
    total_needed: int = 0

    for line in input:
        line: str = line.strip()  # remove newline character at the end

        d: Dimension = parse_line(line)

        total_needed += surface_area(d)
        total_needed += smallest_area(d)

    return total_needed


class TestSolve(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve(["2x3x4"]), 58)

    def test_example2(self):
        self.assertEqual(solve(["1x1x10"]), 43)


def run() -> None:
    run_with_input_lines(2015, 2, 1, sys.modules[__name__])
