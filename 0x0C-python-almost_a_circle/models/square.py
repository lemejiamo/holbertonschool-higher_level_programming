#!/usr/bin/python3
"""  creating the class Square """
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ creating a class Square inherits from class Rectangle"""

    # |-------------- Private Method from class Square --------------------|
    # |---------------------------- CONSTRUCTOR ---------------------------|
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor

            Attributes
            size (integer)
            x (integer)
            y (integer)
            id (interger)
        """
        self.size = size
        super().__init__(size, size, x, y, id)
    # |------------------------ END OF CONSTRUCTOR ------------------------|

    # |-------------- Private Method from class Square --------------------|
    # |---------------------- Override __str__ method ---------------------|
    def __str__(self):
        """ override __str__ magic method"""

        return ("[{}] ({}) {}/{} - {}".format(
                __class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size))
    # |--------------------------- END OF __STR__ -------------------------|

    # |------------------- setter and getter *SIZE* Attribute -------------|
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.integer_validator("width", value)
        self.__size = value
    # |--------------------------- END OF FUNCTION ------------------------|
