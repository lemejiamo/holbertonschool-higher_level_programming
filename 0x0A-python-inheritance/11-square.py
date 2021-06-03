#!/usr/bin/python3
""" a class to make a square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class inheritd froms Rectangle """

    def __init__(square, size):
        """ constructor """

        square.integer_validator("size", size)
        square.__size = size
        super().__init__(size, size)

    def area(square):
        """ calculate the area """

        return square.__size * square.__size

    def __str__(self):
        """ return a string description of object """

        clas = __class__.__name__
        str = ("[{}] {}/{}".format(clas, self.__size, self.__size))
        return str
