#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """Print utf-8 file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
