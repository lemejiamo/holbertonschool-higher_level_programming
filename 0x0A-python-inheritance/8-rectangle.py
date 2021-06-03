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
