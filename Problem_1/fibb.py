#!/usr/bin/env python3

import sys


def usage():
    print("""fibb.py <MAX>

Arguments:
    MAX     The max Fibonacci value.
    """)
    exit()

def get_fibb_sequence(max: int):
    a,b = 0,1

    while a <= max:
        yield a
        a, b = b, a + b

def print_results(generator):
    odds = []

    for i in generator:
        if i % 2:
            odds.append(i)

        if i == 0:
            print(f"{i}", end="")
        else:
            print(f",{i}", end="")

    print(f"\nSum of odds: {sum(odds)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        print(len(sys.argv))

    try:
        MAX = int(sys.argv[1])
    except ValueError:
        usage()

    print_results(get_fibb_sequence(MAX))
        