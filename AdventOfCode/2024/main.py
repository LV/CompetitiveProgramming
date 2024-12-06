from util.argparse import get_puzzle_id_from_argparse, PuzzleID
import importlib
import os

def main():
    """Program startpoint"""

    puzzle: PuzzleID = get_puzzle_id_from_argparse()

    # Check if puzzle solution file exists before importing
    module_path = os.path.join("solutions", str(puzzle.year), f"{puzzle.day}-{puzzle.part}.py")
    if not os.path.exists(module_path):
        raise NotImplementedError(f"AoC {puzzle.year} day {puzzle.day} part {puzzle.part} has not been solved yet.")

    solution_module = importlib.import_module(f"solutions.{puzzle.year}.{puzzle.day}-{puzzle.part}")
    if not hasattr(solution_module, "solve"):
        raise AttributeError(f"solutions/{puzzle.year}/{puzzle.day}-{puzzle.part}.py has no `solve()` function.")


if __name__ == "__main__":
    main()
