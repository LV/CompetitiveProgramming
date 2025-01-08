from util.argparse import get_puzzle_id_from_argparse, PuzzleID
import importlib
import os

def main():
    """Program startpoint"""

    puzzle: PuzzleID = get_puzzle_id_from_argparse()

    # Check if puzzle solution file exists before importing
    module_path = os.path.join("solutions", f"{puzzle.year}", f"day{puzzle.day:02}-{puzzle.part}.py")
    if not os.path.exists(module_path):
        raise NotImplementedError(f"AoC {puzzle.year} day {puzzle.day} part {puzzle.part} has not been solved yet.")

    solution_module = importlib.import_module(f"solutions.{puzzle.year}.day{puzzle.day:02}-{puzzle.part}")
    if not hasattr(solution_module, "run"):
        raise AttributeError(f"solutions/{puzzle.year}/day{puzzle.day:02}-{puzzle.part}.py has no `run()` fuction.")

    solution_module.run()


if __name__ == "__main__":
    main()
