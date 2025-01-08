#!/usr/bin/env python3
import pathlib

file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "input" / "05.txt"


def has_sandwich_str(inp: str):
    for i in range(len(inp) - 2):
        curr: str = inp[i : i + 3]

        if curr[0] == curr[2]:
            return True

    return False


def generate_pair_list(inp: str) -> list[str]:
    final_list: list[str] = []
    last_pair: str = ""

    for i in range(len(inp) - 1):
        curr_pair: str = inp[i : i + 2]

        # Discard overlapping, can only happen with repeated letters
        if curr_pair == last_pair:
            last_pair = ""
            continue

        last_pair = curr_pair
        final_list.append(curr_pair)

    return final_list


def has_repeating_pairs(inp: str) -> bool:
    pair_list: list[str] = generate_pair_list(inp)

    pair_list.sort()

    for i in range(len(pair_list) - 1):
        if pair_list[i] == pair_list[i + 1]:
            return True

    return False


def is_nice_string(inp: str) -> bool:
    return has_repeating_pairs(inp) and has_sandwich_str(inp)


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
