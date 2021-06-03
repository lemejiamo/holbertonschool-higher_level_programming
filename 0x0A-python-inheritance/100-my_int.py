#!/usr/bin/python3
""" creating  MyInt class. """


class MyInt(int):
    """ My Int inherits from int """

    def __init__(self, number):
        self.number = number

    def __eq__(self, number):
        """ not equal to """
        return int(self) != number

    def __ne__(self, number):
        """ equal to """
        return int(self) == number
