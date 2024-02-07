#!/usr/bin/python3
""" Module for string object to JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Save JSON of string object """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
