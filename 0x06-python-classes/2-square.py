#!/usr/bin/python3
"""Square 
    Learning attributes works into a classes
    and objects
"""

class Square():
    """Class square define a square

       __init__ initialization of private instance
    """
    def __init__(self, size=0):
        """ constructor
            to create a square

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
