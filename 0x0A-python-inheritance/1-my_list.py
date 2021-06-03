#!/usr/bin/python3
""" function to print list sorted."""


class MyList(list):
    """ class make task with list."""

    def print_sorted(self):
        """print sorted method."""
        print(sorted(self))
