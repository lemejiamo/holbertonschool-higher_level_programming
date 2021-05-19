#!/usr/bin/python3
"""Square
   Learning attributes works into a classes
   and objects
"""


class Square():
    """Class square define a square

       __init__ initialization of private instance
    """
    def __init__(self, size=0, position=(0, 0)):
        """ constructor
            to create a square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
            calculate a area of square
        """
        self.area = (self.__size * self.__size)
        return self.area

    def my_print(self):
        new_lines = spaces = 0

        if type(self.position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        if self.position != 0:
                new_lines, spaces = self.position[1], self.position[0]

        j = 0
        while j < new_lines:
            print()
            j += 1

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                j = k = 0
                while k < self.size:
                    while j < spaces:
                        print(' ', end="")
                        j += 1
                    print("#", end="")
                    k += 1
                print()
