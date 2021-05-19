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
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            calculate a area of square
        """
        self.area = (self.__size * self.__size)
        return self.area

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            i = 0
            while i <= self.size:
                print("#", end="")
                i += 1
            print()
