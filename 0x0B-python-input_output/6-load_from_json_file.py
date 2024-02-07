#!/usr/bin/python3
""" Module to read from JSON file """
import json


def load_from_json_file(filename):
    """ Return object from JSON file """
    with open(filename) as f:
        return json.load(f)
