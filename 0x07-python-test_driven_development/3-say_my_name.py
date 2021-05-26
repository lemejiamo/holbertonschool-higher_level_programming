#!/usr/bin/python3
"""
    a function that prints two strings
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name
        this function concatena two strings to
        make a full name from anybody

        Attributes

        first_name = first string
        last_name = second string empty by default
    """

# validation of input data
    if type(first_name) != str or first_name == "":
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
