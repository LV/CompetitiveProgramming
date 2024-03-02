import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "01.txt"
f = open(file_path, "r")


def main() -> None:
    i: int = 0
    j: int = 0

    for char in f.read():
        j += 1
        if char == "(":
            i += 1
        elif char == ")":
            i -= 1
        if i < 0:
            print(j)
            break


if __name__ == "__main__":
    main()
