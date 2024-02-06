#!/usr/bin/python3
""" Module for `is_same_class` function """


def is_same_class(obj, a_class):
    """ is `obj` is an instance of `a_class` """
    return type(obj) is a_class
