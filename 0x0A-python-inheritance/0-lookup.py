#!/usr/bin/python3
""" function to get the attributes and methods from object"""


def lookup(obj):
    """

    :param obj: object to analice
    :return: list of attributes and methods from a object
    """
    return dir(obj)
