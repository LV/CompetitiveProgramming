import importlib
import pathlib
import unittest

def _get_input_string(year: int, day: int) -> str:
    file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "inputs" / f"{year}" / f"day{day:02}.txt"
    return file_path.read_text(encoding="utf-8")

def run_with_input_string(year: int, day: int, part: int, test_module):
    """Abstracted runner for Advent of Code solutions"""
    # Run the tests
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(test_module))
    if result.wasSuccessful():
        # Dynamically load the solve function
        solve_module = importlib.import_module(f"solutions.{year}.day{day:02}-{part}")
        if not hasattr(solve_module, "solve"):
            raise AttributeError(f"Module solutions.{year}.day{day:02}-{part} does not have a `solve` function.")
        solve_function = solve_module.solve
        # Pass input to solve function and print result
        input_string = _get_input_string(year, day)
        print(f"ANSWER: {solve_function(input_string)}")
    else:
        print("Tests failed!")
