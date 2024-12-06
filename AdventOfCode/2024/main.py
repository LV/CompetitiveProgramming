from util.argparse import get_problem_id_from_argparse, ProblemID

def main():
    """Program startpoint"""

    problem: ProblemID = get_problem_id_from_argparse()

if __name__ == "__main__":
    main()
