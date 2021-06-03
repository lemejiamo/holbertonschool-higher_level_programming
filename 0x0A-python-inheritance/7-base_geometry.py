#!/usr/bin/python3
""" class to learn python project 0x0A Holberton School """


class BaseGeometry():
    """ a class to develop"""

    def area(self):
        """ not implemented yet """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validation of a integer """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} ust be greater than 0".format(name))
