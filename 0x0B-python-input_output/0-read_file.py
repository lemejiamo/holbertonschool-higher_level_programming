#!/usr/bin/python3
"""this function goint to read a text file and write his contents in a STDOUT
"""


def read_file(filename=""):
    """ Read line by line in a file and print in STDOUT


        ARGS:
            filename: string name to the file
    """

    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            print(line, end='')
