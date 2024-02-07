#!/usr/bin/python3
""" Module for class to JSON """


def class_to_json(obj):
    """ Return dict of simple obj """
    return obj.__dict__
