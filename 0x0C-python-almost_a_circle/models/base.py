#!/usr/bin/python3
""" Base class """
import json
import csv


class Base():
    """ Base class to Holberton project almost a circle """

    # |--------------- PRIVATE ATTRIBUTES FROM  CLASS BASE ----------------|

    __nb_objects = 0
    auto_id = 0

    # |----------------- PRIVATE METHOD FROM  CLASS BASE ------------------|
    # |---------------------------- CONSTRUCTOR ---------------------------|
    def __init__(self, id=None):
        """ __init__: constructor

            Attributes:
            id: integer that identifies a new instance
        """

        Base.__nb_objects += 1

        if id is None:
            Base.auto_id += 1
            self.id = Base.auto_id
        elif id <= 0:
            Base.auto_id += 1
            self.id = Base.auto_id
        else:
            self.id = id
    # |-------------------------- END OF FUNCTION -------------------------|

    # |---------------- STATIC METHOD'S FROM  CLASS BASE ------------------|
    # |------------------------- TO_JSON_STRING ---------------------------|
    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert a dictionary to JSON string"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------- STATIC METHOD'S FROM  CLASS BASE ---------------------|
    # |----------------------- FROM_JSON_STRING ---------------------------|
    @staticmethod
    def from_json_string(json_string):
        """ return a JSON string"""

        if json_string == [] or json_string is None:
            return "[]"
        return json.loads(json_string)
    # |-------------------------- END OF FUNCTION -------------------------|

    # |----------------- CLASS METHOD'S FROM  CLASS BASE ------------------|
    # |-------------------------- SAVE_TO_FILE ----------------------------|

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of objects into a JSON file

            Attributes:
            list_objs: list of objects to save in a JSON file
        """

        file = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs == [] or list_objs is None:
            string = cls.to_json_string(list_dictionaries)
        else:
            for i in list_objs:
                list_dictionaries.append(cls.to_dictionary(i))

        with open(file, 'w') as file:
            string = cls.to_json_string(list_dictionaries)
            file.write(string)
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------------------------ CREATE ------------------------------|
    @classmethod
    def create(cls, **dictionary):
        """ create a object from dictionary"""

        name = "{}".format(cls.__name__)

        if name == "Square":
            square = cls(1)
            square.update(**dictionary)
            return square

        elif name == "Rectangle":
            rectangle = cls(1, 1)
            rectangle.update(**dictionary)
            return rectangle
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------------ CLASS METHOD'S FROM  CLASS BASE -----------------|
    # |-------------------------- LOAD_FROM_FILE --------------------------|

    @classmethod
    def load_from_file(cls):
        """ loas a objects from JSON file """

        file = "{}.json".format(cls.__name__)
        obj_list = []
        try:
            with open(file, 'r') as open_file:
                data = json.load(open_file)
                # cls.from_json_string(open_file.read())
                for obj in data:
                    obj_list.append(cls.create(**obj))
                return obj_list
        except:
            return []
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------------ CLASS METHOD'S FROM  CLASS BASE -----------------|
    # |------------------------- SAVE_TO_FILE_CSV -------------------------|
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves a list of objects into a CSV file

            Attributes:
            list_objs: list of objects to save in a JSON file
        """

        file = "{}.csv".format(cls.__name__)

        dict_list = []
        # convert the list_objs to list with dictionary description
        for i in list_objs:
            dictionary_obj = cls.to_dictionary(i)
            dict_list.append(dictionary_obj)

        # create the csv file
        with open(file, 'w', newline='') as file:
            to_csv = csv.writer(file)  # makes te file available to write in it
            count = 0
            for i in dict_list:
                if count == 0:
                    to_csv.writerow(i.keys())
                    count += 1
                to_csv.writerow(i.values())
    # |-------------------------- END OF FUNCTION -------------------------|

    # |------------------ CLASS METHOD'S FROM  CLASS BASE -----------------|
    # |------------------------ LOAD_FROM_FILE_CSV ------------------------|

    @classmethod
    def load_from_file_csv(cls):
        """  load objects from csv file"""

        file = "{}.csv".format(cls.__name__)

        list_objs = []
        Headers = []
        with open(file, 'r', newline='') as file:
            from_csv = csv.reader(file)
            count = 0
            for row in from_csv:
                if count == 0:
                    Headers = row
                    count += 1
                else:
                    dict = {}
                    for i in range(len(row)):
                        dict[Headers[i]] = int(row[i])
                    list_objs.append(cls.create(**dict))
            return list_objs

    # |-------------------------- END OF FUNCTION -------------------------|
