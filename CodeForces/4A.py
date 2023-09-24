#!/usr/bin/env python3

"""
4A: Watermelon
https://codeforces.com/problemset/problem/4/A
"""

def main():
    # Read input
    n = int(input().strip())

    # bin() function converts 'n' to string and appends '0b' to string
    # EXAMPLE: bin(10) --> '0b1010'
    #
    # Check if final bit is set to 0 (i.e. if it is odd or not)
    # 2 is the only number (1 <= w <= 100) that cannot have two separate even halfs
    if bin(n)[n.bit_length()+1] == '0' and n != 2:
        print("YES")

    else:
        print("NO")

if __name__ == "__main__":
    main()
