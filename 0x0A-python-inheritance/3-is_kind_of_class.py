#!/usr/bin/python3
""" Module for checking class membership """


def is_kind_of_class(obj, a_class):
    """ Checks if obj is an instance of a_class or a subclass
    Returns: True if obj is an instance of a_class or subclass
    """
    return isinstance(obj, a_class)
