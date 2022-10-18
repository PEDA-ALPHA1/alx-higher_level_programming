#!/usr/bin/python3
"""
prints square using #'s
Takes in an integer size
"""


def print_square(size):
    """
    Prints square with #'s given int size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
