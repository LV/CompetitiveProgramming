#!/usr/bin/env python3
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.resolve() / "05.txt"


def is_vowel(char: str) -> bool:
    if len(char) != 1:
        raise ValueError("Input is too long!")

    return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"


def has_at_least_three_vowels(inp: str) -> bool:
    vowel_count: int = 0

    for char in inp:
        if is_vowel(char):
            vowel_count += 1

    return vowel_count >= 3


def has_doubled_letters(inp: str) -> bool:
    # Get the pairs on the current and next index
    for i in range(len(inp) - 1):
        curr: str = inp[i : i + 2]

        if curr[0] == curr[1]:
            return True

    return False


def is_excluded(inp: str) -> bool:
    return inp == "ab" or inp == "cd" or inp == "pq" or inp == "xy"


def has_excluded_string(inp: str) -> bool:
    # Get the pairs on the current and next index
    for i in range(len(inp) - 1):
        curr: str = inp[i : i + 2]

        if is_excluded(curr):
            return True

    return False


def is_nice_string(inp: str) -> bool:
    return (
        has_at_least_three_vowels(inp)
        and has_doubled_letters(inp)
        and (not has_excluded_string(inp))
    )


def main() -> None:
    nice_string_count: int = 0

    with open(file_path, "r") as f:
        for line in f:
            line: str = line.strip()  # remove newline character at the end
            if is_nice_string(line):
                nice_string_count += 1

    print(nice_string_count)


if __name__ == "__main__":
    main()
