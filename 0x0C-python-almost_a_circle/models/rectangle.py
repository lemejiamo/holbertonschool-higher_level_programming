#!/usr/bin/python3
"""  creating the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from class Base """
    # |---------------- ATTRIBUTES FROM RECTANGLE CLASS -------------------|

    print_symbol = '#'

    # |-------------- PRIVATE METHOD FROM  CLASS RECTANGLE ----------------|
    # | --------------------------- CONSTRUCTOR ---------------------------|
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ (constructor)

        Attributes:
            id (integer): unique identifier of the object
            width (integer)
            height (integer)
            x (integer)
            y (integer)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    # |------------------------ END OF CONSTRUCTOR ------------------------|

    # |-------------- PRIVATE METHOD FROM  CLASS RECTANGLE ----------------|
    # |--------------------- OVERRIDE __STR__ METHOD ----------------------|
    def __str__(self):
        """ Print the string representation of instance """

        return ("[{}] ({}) {}/{} - {}/{}".format(
                __class__.__name__,
                self.id,
                self.x,
                self.y,
                self.width,
                self.height))
    # |------------------------- END OF FUNCTION --------------------------|

    # |-------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ---------------|
    # |----------------- FUNCTION TO VALIDATE INPUT DATA ------------------|
    def integer_validator(self, name, value):
        """ Validation of a integer

            Attributes:
            name (str): name from attribute to analice
            valur (int): value of attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value == 0 and (name == "y" or name == "x"):
            return
        if value <= 0:
            if (name == "y" or name == "x"):
                raise ValueError("{} must be >= 0".format(name))
            raise ValueError("{} must be > 0".format(name))
    # |------------------------- END OF FUNCTION --------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |------------------ FUNCTION TO CALCULATE THE AREA ------------------|
    def area(self):
        """ Calculates a area """

        return self.width * self.height
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |------------------- FUNCTION TO DISPLAY RECTANGLE ------------------|
    def display(self):
        """ Print a rectangle with # """

        rectangle = ""
        if (self.height == 0 or self.width == 0):
            return rectangle
        y, x = self.y, self.x

        while y:
            rectangle += '\n'
            y -= 1

        for i in range(self.height):
            j = k = 0
            while k < self.width:
                while j < self.x:
                    rectangle += (str(' '))
                    j += 1
                rectangle += (str(self.print_symbol))
                k += 1
            if i + 1 < self.height:
                rectangle += '\n'

        print(rectangle)
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |---------------------- UPDATE RECTANGLE values ---------------------|
    def update(self, *args, **kwargs):
        """ Update instance with the given data

            Attributes:
            *args (list): list of values to update
            **kwargs (dict): dict of values to update,
            dont works if *args is passed
        """

        fields = ["size", "height", "width", "x", "y", "id"]

        if len(args) != 0 and len(args) > 0:
            # entry point to *args ----------------------------------------|
            if len(args) >= 1:
                super().__init__(args[0])

            if len(args) >= 2:

                if (type(self) == Rectangle):
                    self.width = args[1]
                else:
                    self.size = args[1]

            if len(args) >= 3:
                if (type(self) == Rectangle):
                    self.height = args[2]
                else:
                    self.x = args[2]

            if len(args) >= 4:
                if (type(self) == Rectangle):
                    self.x = args[3]
                else:
                    self.y = args[3]

            if len(args) >= 5:
                if (type(self) == Rectangle):
                    self.y = args[4]
                pass

        # entry point to **kwargs -----------------------------------------|
        else:
            for key in kwargs:
                if key in fields:
                    setattr(self, key, kwargs[key])

    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |--------------------------- TO_DICTIONARY --------------------------|
    def to_dictionary(self):
        """ Print dictionary representation of a instance """

        if (type(self) == Rectangle):
            rectangle_dict = {
                'x': self.x,
                'y': self.y,
                'width': self.width,
                'height': self.height,
                'id': self.id}
            return rectangle_dict
        else:
            square_dict = {
                'x': self.x,
                'y': self.y,
                'size': self.size,
                'id': self.id}
            return square_dict
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |-------------------- set and get *width* Attribute -----------------|
    @property
    def width(self):
        """Getter of the Rectangle width value"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter of the Rectangle width value"""

        self.integer_validator("width", value)
        self.__width = value
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |------------------ set and get *height* Attribute ------------------|
    @property
    def height(self):
        """Getter of the Rectangle height value"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter of the Rectangle height value"""

        self.integer_validator("height", value)
        self.__height = value
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |--------------------- set and get *x* Attribute --------------------|
    @property
    def x(self):
        """Getter of the instance 'X' value"""

        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter of the instance 'X' value"""

        self.integer_validator("x", value)
        self.__x = value
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- PUBLIC METHOD'S FROM  CLASS RECTANGLE ----------------|
    # |--------------------- set and get *y* Attribute --------------------|
    @property
    def y(self):
        """Getter of the instance 'Y' value"""

        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter of the instance 'Y' value"""

        self.integer_validator("y", value)
        self.__y = value
    # |-------------------------- END OF FUNCTION -------------------------|
