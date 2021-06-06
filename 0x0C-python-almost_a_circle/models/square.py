#!/usr/bin/python3
"""  creating the class Square """
from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle):
    """ creating a class Square inherits from class Rectangle"""

# CONSTRUCTOR ---------------------------------------------------------|
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor

            Attributes
            size (integer)
            x (integer)
            y (integer)
            id (interger)
        """
        super().__init__(size, size, x, y, id)

# END OF CONSTRUCTOR ----------------------------------------------------|



