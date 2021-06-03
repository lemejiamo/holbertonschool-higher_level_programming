#!/usr/bin/python3
"""  a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """ add attribute """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
