#!/usr/bin/python3
"""this function goint to read a text file and write his contents in a STDOUT
"""


def read_file(filename=""):
    """ Read line by line in a file and print in STDOUT
    """

    file = open(filename, "r")

    for line in file:
        print(line, end='')
