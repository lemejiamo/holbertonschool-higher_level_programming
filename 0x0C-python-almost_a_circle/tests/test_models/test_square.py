
#!/usr/bin/python3
""" Test module for storing Square class test cases. """
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO
from time import sleep
import os
print_on = 0  # <-- Set to 1 to activate printing of the tests.


class TestSquare(unittest.TestCase):
    """ TestSquare class for storing the unittest methods and cases. """
    if print_on == 1:
        green = "\033[92m"  # <-- Stores the green text color format.
        reset = "\033[0m"  # <-- Stores the reset text color format.
        print(green + "." + "~ " * 11 + "| test_square.py module. |" +
              "~ " * 11 + reset)
        sleep(1)

    # Tests from 9-main.py ---------------------------------------------------|
    def test_9_Square(self):
        """ Test cases for Square class objects, from 9-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 9-main.py " +
                  "~" * 19 + reset)

        s1 = Square(5)
        # Test print(s1)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 25
        self.assertEqual(s1.area(), 25)

        # Test .display()
        case_string = "#####\n" * 5
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        s2 = Square(2, 2)
        # Test print(s2)
        case_string = "[Square] (2) 2/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 4
        self.assertEqual(s2.area(), 4)

        # Test .display()
        case_string = "  ##\n" * 2
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        s3 = Square(3, 1, 3)
        # Test print(s3)
        case_string = "[Square] (3) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s3)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .area() == 9
        self.assertEqual(s3.area(), 9)

        # Test .display()
        case_string = "\n" * 3 + " ###\n" * 3
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Tests from 10-main.py --------------------------------------------------|
    def test_10_Square(self):
        """ Test cases for Square class objects, from 10-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 10-main.py " +
                  "~" * 18 + reset)

        s1 = Square(5)
        # Test print(s1)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .size()
        self.assertEqual(s1.size, 5)

        s1.size = 10
        case_string = "[Square] (1) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test pass a "string" to size.
        with self.assertRaises(TypeError):
            s1.size = "9"

    # Tests from 11-main.py --------------------------------------------------|
    def test_11_Square(self):
        """ Test cases for Square class objects, from 11-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 11-main.py " +
                  "~" * 18 + reset)

        # Test Create a Square
        s1 = Square(5)
        case_string = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(10)
        s1.update(10)
        case_string = "[Square] (10) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2)
        s1.update(1, 2)
        case_string = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2, 3)
        s1.update(1, 2, 3)
        case_string = "[Square] (1) 3/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(1, 2, 3, 4)
        s1.update(1, 2, 3, 4)
        case_string = "[Square] (1) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(x=12)
        s1.update(x=12)
        case_string = "[Square] (1) 12/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(size=7, y=1)
        s1.update(size=7, y=1)
        case_string = "[Square] (1) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test .update(size=7, id=89, y=1)
        s1.update(size=7, id=89, y=1)
        case_string = "[Square] (89) 12/1 - 7\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test from 13-main.py - update(**kwargs) --------------------------------|
    def test_13_Squares(self):
        """ Test cases for Square class objects, from 13-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 13-main.py " +
                  "~" * 19 + reset)

        s1 = Square(10, 2, 1)
        case_string = "[Square] (1) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Return Dictionary
        s1_dictionary = s1.to_dictionary()
        case_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        # Test if the dictionary is the correct one.
        self.assertEqual(s1_dictionary, case_dict)
        # Test the type of the return.
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        case_string = "[Square] (2) 1/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        s2.update(**s1_dictionary)
        case_string = "[Square] (1) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test that r1 is different tha r2
        self.assertFalse(s1 == s2)

    # Copy for Square of Tests from 1-main.py --------------------------------|
    def test_1_Square(self):
        """ Test cases for Square class objects, from 1-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 19 + " Testing cases from 1-main.py " +
                  "~" * 19 + reset)

        r1 = Square(10)
        self.assertEqual(r1.id, 1)

        r2 = Square(2)
        self.assertEqual(r2.id, 2)

        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    # Copy for Square of Tests from 2-main.py --------------------------------|
    def test_2_Square(self):
        """ Test cases for Square class objects, from 2-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 2-main.py " +
                  "~" * 19 + reset)

        with self.assertRaises(TypeError):
            s = Square(10, "2")

        with self.assertRaises(ValueError):
            s = Square(10, 2)
            s.width = -10

        with self.assertRaises(TypeError):
            s = Square(10, 2)
            s.x = {}

        with self.assertRaises(ValueError):
            Square(10, 2, -1)

    # Copy for Square of Tests from 3-main.py --------------------------------|
    def test_3_Square(self):
        """ Test cases for Square class objects, from 3-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 3-main.py " +
                  "~" * 19 + reset)

        s1 = Square(3, 2)
        self.assertEqual(s1.area(), 9)

        s2 = Square(2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(8)
        self.assertEqual(s3.area(), 64)

    # Copy for Square of Test from 4-main.py ---------------------------------|
    def test_4_Squares(self):
        """ Test cases for Square class objects, from 4-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 4-main.py " +
                  "~" * 19 + reset)

        # Test display Square(4)
        case_string = ("####\n" * 4)
        r = Square(4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test display Square(2)
        case_string = ("##\n" * 2)
        r = Square(2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Copy for Square of Test from 5-main.py ---------------------------------|
    def test_5_Squares(self):
        """ Test cases for Square class objects, from 5-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 5-main.py " +
                  "~" * 19 + reset)

        # Test display Square(4, 2, 1, 12)
        case_string = "[Square] (12) 2/1 - 4\n"
        r1 = Square(4, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test print Square(5, 5, 1)
        case_string = "[Square] (1) 5/1 - 5\n"
        r2 = Square(5, 5, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test, str()
        a = str(r1)
        self.assertEqual(a, "[Square] (12) 2/1 - 4")

        # Test, str()
        a = str(r2)
        self.assertEqual(a, "[Square] (1) 5/1 - 5")

    # Copy for Square of Test from 6-main.py ---------------------------------|
    def test_6_Squares(self):
        """ Test cases for Square class objects, from 6-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 6-main.py " +
                  "~" * 19 + reset)

        # Test display Square(2, 3, 2, 2)
        case_string = "\n\n" + "   ##\n" * 2
        r = Square(2, 3, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test display Square(3)
        case_string = '\n' + "  ###\n" * 3
        r = Square(3, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), case_string)

    # Copy for Square of Test from 7-main.py - update(*args) -----------------|
    def test_7_Squares(self):
        """ Test cases for Square class objects, from 7-main.py"""
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 20 + " Testing cases from 7-main.py " +
                  "~" * 19 + reset)

        # Test Square(10, 10, 10, 10)
        case_string = "[Square] (10) 10/10 - 10\n"
        r1 = Square(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89)
        case_string = "[Square] (89) 10/10 - 10\n"
        r1.update(89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2)
        case_string = "[Square] (89) 10/10 - 2\n"
        r1.update(89, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3)
        case_string = "[Square] (89) 3/10 - 2\n"
        r1.update(89, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3, 4)
        case_string = "[Square] (89) 3/4 - 2\n"
        r1.update(89, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

        # Test update(89, 2, 3, 4, 5)
        case_string = "[Square] (89) 3/4 - 2\n"
        r1.update(89, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), case_string)

    # Test for update() method.
    def test_Square_update(self):
        """ Test cases for the .display() """
        if print_on == 1:
            green = "\033[92m"
            reset = "\033[0m"
            print(green + "~" * 19 + " Testing Square.update() method. " +
                  "~" * 17 + reset)

        # Case when both *args and **kwargs are used.
        s = Square(1)
        s.update(2, id=100)  # <-- expected to remain unaltered by kwargs.
        case_string = "[Square] (2) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s)
            self.assertEqual(fake_out.getvalue(), case_string)

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
