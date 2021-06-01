#!/usr/bin/python3
"""defina a class Student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """" initialitation of class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ show a class like a dictionary"""
        return self.__dict__
