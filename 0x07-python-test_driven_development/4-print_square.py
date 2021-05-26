#!/usr/bin/python3
"""
    a function to print a square with #
"""


def print_square(size):
    """
        attributes:
        size: a size of square
    """

    # validation of size value
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
