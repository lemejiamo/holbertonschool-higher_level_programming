#!/usr/bin/python3
""" class to learn python project 0x0A Holberton School """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define a class Rectangle inherits from  BaseGeometry"""

    def __init__(self, width, height):
        """ constructor

        Attributes:
            width: Private
            height: Private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates a area """

        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
