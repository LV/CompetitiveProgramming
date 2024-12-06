from util.argparse import get_problem_id_from_argparse, ProblemID
import importlib
import os

def main():
    """Program startpoint"""

    problem: ProblemID = get_problem_id_from_argparse()

    # Check if problem solution file exists before importing
    module_path = os.path.join("solutions", str(problem.year), f"{problem.question}-{problem.part}.py")
    if not os.path.exists(module_path):
        raise NotImplementedError(f"AoC {problem.year} question {problem.question} part {problem.part} has not been solved yet.")

    solution_module = importlib.import_module(f"solutions.{problem.year}.{problem.question}-{problem.part}")
    if not hasattr(solution_module, "solve"):
        raise AttributeError(f"solutions/{problem.year}/{problem.question}-{problem.part}.py has no `solve()` function.")


if __name__ == "__main__":
    main()
