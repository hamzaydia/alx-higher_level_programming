#!/usr/bin/python3
""" Module for JSON to object """
import json


def from_json_string(my_str):
    """Return the object of the provided JSON string """
    return json.loads(my_str)
