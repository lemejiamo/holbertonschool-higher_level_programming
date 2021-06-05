#!/usr/bin/python3
""" Base class """


class Base():
    """ more context """
    # attributes of *class*
    __nb_objects = 0
    auto_id = 0

    # methods of the *class*
    def __init__(init__, id=None): # private method
        """ __init__: constructor
        
            Attributes:
            id: integer that identifies a new instance
        """
        Base.__nb_objects += 1

        if id is None:
            Base.auto_id += 1
            init__.id = Base.auto_id
        else:
            init__.id = id
