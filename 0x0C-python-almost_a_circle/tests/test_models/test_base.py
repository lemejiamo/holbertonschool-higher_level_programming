#!/usr/bin/python3
""" Test module for base.py """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO
import os


class TestBase(unittest.TestCase):
    """ TestBase  for test class Base. """

    def test_0_Base(self):
        """ Tests the cases for the Base class from 0-main.py """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_14_Base(self):
        """ Tests the cases for the Base class from 14-main.py """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string(sorted(dictionary.items()))
        case = '[["height", 7], ["id", 1], ["width", 10], ["x", 2], ["y", 8]]'
        self.assertEqual(json_string, case)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_string), str)

        empty = Base.to_json_string(None)
        self.assertEqual(empty, "[]")

        empty = Base.to_json_string([])
        self.assertEqual(empty, "[]")

    def test_15_Base(self):
        """ Tests the cases for the Base class from 15-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 15-main.py " +
                  "~" * 19 + reset)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        sum_save = 0
        case = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, ' +
                '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')

        sum_expected = sum(list(map(lambda letter: ord(letter), case)))

        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                sum_save = sum(list(map(lambda letter: ord(letter),
                                        file.read())))
            self.assertEqual(sum_save, sum_expected)

        r3 = Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_16_Base(self):
        """ Tests the cases for the Base class from 16-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 16-main.py " +
                  "~" * 19 + reset)
        # Main case.
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

        # If json_string None
        list_input = None
        json_string = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_output, [])

        # If json_string empty
        list_input = []
        json_string = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_output, [])

    def test_17_Base(self):
        """ Tests the cases for the Base class from 17-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 17-main.py " +
                  "~" * 19 + reset)

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        case_string = '[Rectangle] (1) 1/0 - 3/5\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
        self.assertEqual(fake_out.getvalue(), case_string)

        case_string = '[Rectangle] (1) 1/0 - 3/5\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
        self.assertEqual(fake_out.getvalue(), case_string)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_18_Base(self):
        """ Tests the cases for the Base class from 18-main.py """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + '.' + "~" * 20 + " Testing cases from 18-main.py " +
                  "~" * 19 + reset)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        case_string_1 = '[Rectangle] (1) 2/8 - 10/7\n'
        case_string_2 = '[Rectangle] (2) 0/0 - 2/4\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_rectangles_output[0])
            self.assertEqual(fake_out.getvalue(), case_string_1)

        self.assertFalse(r1 == list_rectangles_output[0])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_rectangles_output[1])
            self.assertEqual(fake_out.getvalue(), case_string_2)

        self.assertFalse(r1 == list_rectangles_output[0])

        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        case_string_1 = '[Square] (5) 0/0 - 5\n'
        case_string_2 = '[Square] (6) 9/1 - 7\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_squares_output[0])
            self.assertEqual(fake_out.getvalue(), case_string_1)

        self.assertFalse(s1 == list_squares_output[0])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_squares_output[1])
            self.assertEqual(fake_out.getvalue(), case_string_2)

        self.assertFalse(s2 == list_squares_output[1])

    def test_100_Base(self):
        """ Tests the cases for the Base class from 100-main.py """

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        case_string_1 = '[Rectangle] (1) 2/8 - 10/7\n'
        case_string_2 = '[Rectangle] (2) 0/0 - 2/4\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_rectangles_output[0])
            self.assertEqual(fake_out.getvalue(), case_string_1)

        self.assertFalse(r1 == list_rectangles_output[0])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_rectangles_output[1])
            self.assertEqual(fake_out.getvalue(), case_string_2)

        self.assertFalse(r1 == list_rectangles_output[0])

        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        case_string_1 = '[Square] (5) 0/0 - 5\n'
        case_string_2 = '[Square] (6) 9/1 - 7\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_squares_output[0])
            self.assertEqual(fake_out.getvalue(), case_string_1)

        self.assertFalse(s1 == list_squares_output[0])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(list_squares_output[1])
            self.assertEqual(fake_out.getvalue(), case_string_2)

        self.assertFalse(s2 == list_squares_output[1])

    # Tests for the Base class instance. -------------------------------------|
    def test_instance(self):
        """ Test cases for the Base class instance and it's types """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertTrue(type(b1) == Base)


    # Test from Wiston.
    def test_Wis(self):
        """ Checks Contents """
        name = "Rectangle.csv"
        Rectangle.save_to_file_csv([])
        with open(name, "r") as myfile:
            r = myfile.read()
            self.assertEqual(r, '[]')

    # Teardown method for resetting the count of instances in Base class.-----|
    def tearDown(self):
        """ Resets the Base class counter after each test unit. """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass
        try:
            os.remove("Square.json")
        except Exception as e:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception as e:
            pass
        try:
            os.remove("Square.csv")
        except Exception as e:
            pass

if __name__ == '__main__':
    unittest.main()
