#!/usr/bin/python3
""" Module for string object to JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Return JSON of string object """
    return json.dumps(my_obj)
