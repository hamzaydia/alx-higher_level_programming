#!/usr/bin/python3
""" Module containing add_integer function that adds two ints. """


def add_integer(a, b=98):
    """ Sum up two integers and return result. """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
