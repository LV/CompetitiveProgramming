import unittest
from util.input import run_with_input_string
import sys


def solve(input: str) -> int:
    i: int = 0
    j: int = 0

    for char in input:
        j += 1
        if char == "(":
            i += 1
        elif char == ")":
            i -= 1
        if i < 0:
            return j


class TestSolve(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve(")"), 1)

    def test_example2(self):
        self.assertEqual(solve("()())"), 5)


def run() -> None:
    run_with_input_string(2015, 1, 2, sys.modules[__name__])
