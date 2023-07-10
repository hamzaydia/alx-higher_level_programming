#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """Check if obj is instance of a class that
    has a_class as a superclass"""
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
