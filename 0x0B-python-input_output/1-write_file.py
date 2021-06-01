#!/usr/bin/python3
"""learning to return specific info
"""


def write_file(filename="", text=""):
    """

        Attributes:
        filename = string to file to open
        text = a text that you wish to write in a file
    """

    with open(filename, 'w') as file:
        return (file.write(text))
