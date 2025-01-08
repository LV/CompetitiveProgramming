import unittest
from util.input import get_input_string

def solve(input: str) -> int:
    i: int = 0

    for char in input:
        if char == "(":
            i += 1
        elif char == ")":
            i -= 1

    return i


class TestSolve(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve("(())"), 0)

    def test_example2(self):
        self.assertEqual(solve("()()"), 0)

    def test_example3(self):
        self.assertEqual(solve("((("), 3)

    def test_example4(self):
        self.assertEqual(solve("(()(()("), 3)

    def test_example5(self):
        self.assertEqual(solve("))((((("), 3)

    def test_example6(self):
        self.assertEqual(solve("())"), -1)

    def test_example7(self):
        self.assertEqual(solve("))("), -1)

    def test_example8(self):
        self.assertEqual(solve(")))"), -3)

    def test_example9(self):
        self.assertEqual(solve(")())())"), -3)

def run() -> None:
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestSolve))
    if result.wasSuccessful():
        print("ANSWER: " + str(solve(get_input_string(2015, 1))))
    else:
        print("Tests failed!")
