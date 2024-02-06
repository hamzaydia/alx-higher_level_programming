#!/usr/bin/python3
""" Model for add_attribute function """


def add_attribute(obj, att, value):
    """ Add a new attribute to an object. """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
