import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "01.txt"


def get_ints_only(line: str) -> str:
    return [char for char in line if char.isdigit()]


def parse_line(line: str) -> int:
    """
    return only the first and last digits
    """
    line = get_ints_only(line)
    return int(line[0] + line[-1]) if len(line) >= 1 else 0


def main() -> None:
    total: int = 0

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            total += parse_line(line)

    print(total)


if __name__ == "__main__":
    main()
