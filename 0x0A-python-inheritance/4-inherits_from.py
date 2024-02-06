#!/usr/bin/python3
""" Module for checking inheritance """


def inherits_from(obj, a_class):
    """ Checks if `obj` is an instance of a subclass of `a_class`.
    Returns: True if `obj` is an instance of a subclass of `a_class`, False otherwise """
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
