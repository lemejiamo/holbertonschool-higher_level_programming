#!/usr/bin/python3
"""learning to write in a file append method
"""


def append_write(filename="", text=""):
    """

        Attributes:
            filename = string to file to open
            text = a text that you wish to write in a file
    """

    with open(filename, 'a') as file:
        return (file.write(text))
