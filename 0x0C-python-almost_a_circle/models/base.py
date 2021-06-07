#!/usr/bin/python3
""" Base class """
import json


class Base():
    """ more context """

    # |--------------- PRIVATE ATTRIBUTES FROM  CLASS BASE ----------------|

    __nb_objects = 0
    auto_id = 0

    # |----------------- PRIVATE METHOD FROM  CLASS BASE ------------------|
    # |---------------------------- CONSTRUCTOR ---------------------------|
    def __init__(init__, id=None):
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
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- STATIC METHOD'S FROM  CLASS BASE ---------------------|
    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
    # |-------------------------- END OF FUNCTION -------------------------|


    #|-------------- CLASS METHOD'S FROM  CLASS BASE ----------------------|
    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of objects into a JSON file

            Attributes:
            list_objs: list of objects to save in a JSON file
        """

        file = "{}.json".format(cls.__name__)
        list_dictionaries = []
        for i in list_objs:
            list_dictionaries.append(cls.to_dictionary(i))

        with open(file, 'w') as file:
            file.write(json.dumps(list_dictionaries))
    # |-------------------------- END OF FUNCTION -------------------------|
