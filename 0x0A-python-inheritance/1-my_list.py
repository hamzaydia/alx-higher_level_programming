#!/usr/bin/python3
""" Module containing MyList class """


class MyList(list):
    """ class extends functionality from the `list` class. """

    def print_sorted(self):
        """ Prints an int list in ascending order. """
        print(sorted(self))
