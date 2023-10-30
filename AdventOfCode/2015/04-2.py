#!/usr/bin/env python3
import hashlib


def has_leading_six_zeros(inp: bytes) -> bool:
    output: str = hashlib.md5(inp).hexdigest()

    return output[:6] == "000000"


def main() -> None:
    secret_key: str = "ckczppom"
    curr_num: int = 1

    encoded_string: bytes = (secret_key + str(curr_num)).encode()

    while not has_leading_six_zeros(encoded_string):
        curr_num += 1
        encoded_string = (secret_key + str(curr_num)).encode()

    print(curr_num)


if __name__ == "__main__":
    main()
