#!/usr/bin/python3
"""a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer
and boolean) for JSON serialization
of an object
"""


def class_to_json(obj):
    """
    store a object in a json file
    attributes:
        obj: object to store in a json file
    """

    return dict(obj.__dict__)
