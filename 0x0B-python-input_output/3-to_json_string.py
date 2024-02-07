#!/usr/bin/python3
""" Module for string to json """
import json


def to_json_string(my_obj):
    """ Return the json of the string provided """
    return json.dumps(my_obj)
