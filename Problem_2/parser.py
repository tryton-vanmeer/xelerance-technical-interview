#!/usr/bin/env python3

import sys
import csv
import json


def usage():
    print("""parser.py <FILE>

Arguments:
    FILE     The CSV file to parse.
    """)
    exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    FILE = sys.argv[1]

    try:
        with open(FILE) as f:
            reader = csv.reader(f)

            # Use the first row to create a dictionary.
            fieldnames = next(reader)
            reader = csv.DictReader(f, fieldnames)

            for row in reader:
                # Now we can check the province field consistently, even if it
                # isn't always the fourth column.
                if row["Province"] == "Ontario":
                    print(row)
    except FileNotFoundError:
        print(f"No such file: {FILE}")
        exit()