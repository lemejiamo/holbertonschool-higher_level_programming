#!/usr/bin/python3
"""no more a empty class"""


class Rectangle:
    """ start to define a rectangle
        private Attributes:
        __width
        __heigth
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        return (self.__height * self.__width)

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0

        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ print a rectangle with # """
        rectangle = ""
        if (self.height == 0 or self.width == 0):
            return rectangle

        for i in range(self.__height):
            k = 0
            while k < self.__width:
                rectangle += (str(self.print_symbol))
                k += 1
            if i + 1 < self.__height:
                rectangle += '\n'

        return rectangle

    def __repr__(self):

        len_width = str(self.__width)
        len_height = str(self.__height)
        rectan_dimen = "Rectangle(" + len_width + ", " + len_height + ")"
        return rectan_dimen

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
