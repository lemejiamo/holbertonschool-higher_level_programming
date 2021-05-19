#!/usr/bin/python3


class Square():
    """Class square
       Define class square
    """
    def __init__(self, size=0):
        """This function pass size
            as attribute and validate it
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
