#!/usr/bin/python3
"""  creating the class Square """
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ creating a class Square inherits from class Rectangle"""

    # |-------------- PRIVATE METHOD FROM CLASS SQUARE --------------------|
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

    # |-------------- PRIVATE METHOD FROM CLASS SQUARE --------------------|
    # |-----------------------  __STR__ METHOD  ---------------------------|
    def __str__(self):
        """ Print the string representation of instance """

        return ("[{}] ({}) {}/{} - {}".format(
                __class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size))
    # |--------------------------- END OF __STR__ -------------------------|

    # |------------------ PUBLIC METHOD FROM CLASS SQUARE  ----------------|
    # |----------------- SETTER AND GETTER *SIZE* ATTRIBUTE ---------------|
    @property
    def size(self):
        """Getter of the Square size value"""

        return (self.__width)

    @size.setter
    def size(self, value):
        """Setter of the Square size value"""

        self.integer_validator("width", value)
        self.__width = value
    # |--------------------------- END OF FUNCTION ------------------------|
