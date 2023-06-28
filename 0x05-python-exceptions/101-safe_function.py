#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    r = None
    try:
        r = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: " + e.__str__() + "\n")
        return None
    else:
        return r
