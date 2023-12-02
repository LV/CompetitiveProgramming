import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "01.txt"


def check_word(line: str):
    """
    Returns the number of the word, along with the length of the word
    """
    if line[0].isdigit():
        return line[0]

    check: str = ""
    if len(line) >= 3:
        check = line[0:3]
        if check == "one":
            return "1"
        if check == "two":
            return "2"
        if check == "six":
            return "6"
    if len(line) >= 4:
        check = line[0:4]
        if check == "zero":
            return "0"
        if check == "four":
            return "4"
        if check == "five":
            return "5"
        if check == "nine":
            return "9"
    if len(line) >= 5:
        check = line[0:5]
        if check == "three":
            return "3"
        if check == "seven":
            return "7"
        if check == "eight":
            return "8"
    return ""


def convert_words_to_digits(line: str) -> str:
    # Pretty inefficient way of checking words in a string, but I don't have much
    #   time right now and I need to solve this
    line_length: int = len(line)
    final_line: str = ""
    i: int = 0

    while i < line_length:
        final_line += check_word(line[i:])
        i += 1

    return final_line


def get_digits_only(line: str) -> str:
    return [char for char in line if char.isdigit()]


def parse_line(line: str) -> int:
    """
    return only the first and last digits
    """
    line = convert_words_to_digits(line)
    line = get_digits_only(line)
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
