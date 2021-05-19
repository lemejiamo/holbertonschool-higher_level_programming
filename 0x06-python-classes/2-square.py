#!/usr/bin/python3


class Square():
    """Class square define a square

       __init__ initialization of private instance
    """
    def __init__(self, size=0):
        """ constructor
            to create a square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
