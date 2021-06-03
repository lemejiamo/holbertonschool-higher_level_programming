#!/usr/bin/python3
""" a class to make a square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class inheritd froms Rectangle """

    def __init__(square, size):
        """ constructor """

        square.integer_validator("size", size)
        square.size = size
        super().__init__(size, size)

    def area(square):
        """ calculate the area """

        return square.size * square.size
