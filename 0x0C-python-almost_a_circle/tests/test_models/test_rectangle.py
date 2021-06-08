#!/usr/bin/python3
""" Test module for storing Rectangle class test cases. """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
from time import sleep
import os
print_on = 0  # <-- Set to 1 to activate printing of the tests.


class TestRectangle(unittest.TestCase):
    """ TestRectangle class for storing the unittest methods and cases. """
    if print_on == 1:
        green = "\033[92m"  # <-- Stores the green text color format.
        reset = "\033[0m"  # <-- Stores the reset text color format.
        print(green + "." + "~ " * 10 + "~| test_rectangle.py module.| " +
              "~ " * 10 + reset)
        sleep(1)

    # Tests from 1-main.py ---------------------------------------------------|
    def test_1_Rectangle(self):
        """ Test cases for Rectangle class objects, from 1-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 19 + " Testing cases from 1-main.py " +
                  "~" * 19 + reset)

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    # Tests from 2-main.py ---------------------------------------------------|
    def test_2_Rectangle(self):
        """ Test cases for Rectangle class objects, from 2-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 2-main.py " +
                  "~" * 19 + reset)

        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    # Tests from 3-main.py ---------------------------------------------------|
    def test_3_Rectangle(self):
        """ Test cases for Rectangle class objects, from 3-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 3-main.py " +
                  "~" * 19 + reset)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # Test from 4-main.py ----------------------------------------------------|
    def test_4_Rectangles(self):
        """ Test cases for Rectangle class objects, from 4-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 4-main.py " +
                  "~" * 19 + reset)

        # Test display Rectangle(4, 6)
        case_string = ("####\n" * 6)
        r = Rectangle(4, 6)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test display Rectangle(2, 2)
        case_string = ("##\n" * 2)
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 5-main.py ----------------------------------------------------|
    def test_5_Rectangles(self):
        """ Test cases for Rectangle class objects, from 5-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 5-main.py " +
                  "~" * 19 + reset)

        # Test display Rectangle(4, 6, 2, 1, 12)
        case_string = "[Rectangle] (12) 2/1 - 4/6\n"
        r1 = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test print Rectangle(5, 5, 1)
        case_string = "[Rectangle] (1) 1/0 - 5/5\n"
        r2 = Rectangle(5, 5, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test, str()
        a = str(r1)
        self.assertEqual(a, "[Rectangle] (12) 2/1 - 4/6")

        # Test, str()
        a = str(r2)
        self.assertEqual(a, "[Rectangle] (1) 1/0 - 5/5")

    # Test from 6-main.py ----------------------------------------------------|
    def test_6_Rectangles(self):
        """ Test cases for Rectangle class objects, from 6-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 6-main.py " +
                  "~" * 19 + reset)

        # Test display Rectangle(2, 3, 2, 2)
        case_string = "\n\n" + "  ##\n" * 3
        r = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test display Rectangle(3, 2, 1, 0)
        case_string = " ###\n" * 2
        r = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 7-main.py - update(*args) ------------------------------------|
    def test_7_Rectangles(self):
        """ Test cases for Rectangle class objects, from 7-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 7-main.py " +
                  "~" * 19 + reset)

        # Test Rectangle(10, 10, 10, 10)
        case_string = "[Rectangle] (1) 10/10 - 10/10\n"
        r1 = Rectangle(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89)
        case_string = "[Rectangle] (89) 10/10 - 10/10\n"
        r1.update(89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2)
        case_string = "[Rectangle] (89) 10/10 - 2/10\n"
        r1.update(89, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3)
        case_string = "[Rectangle] (89) 10/10 - 2/3\n"
        r1.update(89, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3, 4)
        case_string = "[Rectangle] (89) 4/10 - 2/3\n"
        r1.update(89, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3, 4, 5)
        case_string = "[Rectangle] (89) 4/5 - 2/3\n"
        r1.update(89, 2, 3, 4, 5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 8-main.py - update(**kwargs) ---------------------------------|
    def test_8_Rectangles(self):
        """ Test cases for Rectangle class objects, from 8-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 8-main.py "
                  + "~" * 19 + reset)

        # Test Rectangle(10, 10, 10, 10)
        case_string = "[Rectangle] (1) 10/10 - 10/10\n"
        r1 = Rectangle(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        case_string = "[Rectangle] (1) 10/10 - 10/1\n"
        r1.update(height=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        case_string = "[Rectangle] (1) 2/10 - 1/1\n"
        r1.update(width=1, x=2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        case_string = "[Rectangle] (89) 3/1 - 2/1\n"
        r1.update(y=1, width=2, x=3, id=89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        case_string = "[Rectangle] (89) 1/3 - 4/2\n"
        r1.update(x=1, height=2, y=3, width=4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 12-main.py - update(**kwargs) --------------------------------|
    def test_12_Rectangles(self):
        """ Test cases for Rectangle class objects, from 12-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 12-main.py " +
                  "~" * 19 + reset)

        r1 = Rectangle(10, 2, 1, 9)
        case_string = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Return Dictionary
        r1_dictionary = r1.to_dictionary()
        case_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        # Test if the dictionary is the correct one.
        self.assertEqual(r1_dictionary, case_dict)
        # Test the type of the return.
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        case_string = "[Rectangle] (2) 0/0 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), case_string)

        r2.update(**r1_dictionary)
        case_string = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test that r1 is different tha r2
        self.assertFalse(r1 == r2)

    # Tests for display() method. --------------------------------------------|
    def test_Rectangle_display(self):
        """ Test cases for the .display() """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 17 + " Testing Rectangle.display() method. " +
                  "~" * 15 + reset)

        # Test Rectangle (1, 1)
        case_string = "#\n"
        r = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test Rectangle (2, 3)
        case_string = "##\n" * 3
        r = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test Rectangle (1, 1, 0, 1)
        case_string = "\n#\n"
        r = Rectangle(1, 1, 0, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test Rectangle (1, 1, 1)
        case_string = " #\n"
        r = Rectangle(1, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test Rectangle (1, 1)
        case_string = "#\n"
        r = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test for update() method.
    def test_Rectangle_update(self):
        """ Test cases for the .display() """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 17 + " Testing Rectangle.update() method. " +
                  "~" * 16 + reset)

        # Case when both *args and **kwargs are used.
        r = Rectangle(1, 1)
        r.update(2, id=100)
        case_string = "[Rectangle] (2) 0/0 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test Instance cases ----------------------------------------------------|
    def test_Rectangle_instance(self):
        """ Instance test cases for Rectangle class objects. """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 15 +
                  " Testing Rectangle class instance cases. " +
                  "~" * 13 + reset)

        r = Rectangle(1, 1)
        self.assertTrue(issubclass(type(r), Base))

    # Test Error cases -------------------------------------------------------|
    def test_Rectangle_raises(self):
        """ Error test cases for Rectangle class objects. """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 19 + " Testing Rectangle raise cases. "
                  + "~" * 18 + reset)

        # More arguments than needed.
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

        # Less arguments than needed.
        with self.assertRaises(TypeError):
            r = Rectangle(1)

        # Test for .update()
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1)
            r.update(1, -1, -1)

        # Tests .to_dictionary
        with self.assertRaises(AttributeError):
            r = None
            r.to_dictionary()

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
