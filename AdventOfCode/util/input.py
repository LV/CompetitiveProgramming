import importlib
import pathlib
import unittest

def _get_input_string(year: int, day: int) -> str:
    file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "inputs" / f"{year}" / f"day{day:02}.txt"
    return file_path.read_text(encoding="utf-8")

def run_with_input_string(year: int, day: int, part: int, unittest_module):
    """Abstracted runner for Advent of Code solutions"""
    # Run the tests
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(unittest_module))
    if result.wasSuccessful():
        solve_module = importlib.import_module(f"solutions.{year}.day{day:02}-{part}")
        solve_module = solve_module.solve
        print(f"ANSWER: {solve_module(_get_input_string(year, day))}")
    else:
        print("Tests failed!")
