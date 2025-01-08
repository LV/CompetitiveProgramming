import pathlib

test_file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "01-t1.txt"
input_file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "01-i.txt"


def get_ints_only(line: str) -> str:
    return [char for char in line if char.isdigit()]


def parse_line(line: str) -> int:
    """
    return only the first and last digits
    """
    line = get_ints_only(line)
    return int(line[0] + line[-1]) if len(line) >= 1 else 0


def solve(inp: pathlib.Path) -> int:
    total: int = 0

    with open(inp, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            total += parse_line(line)

    return total


def main() -> None:
    assert solve(test_file_path) == 142
    print(solve(input_file_path))


if __name__ == "__main__":
    main()
