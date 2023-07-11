#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """Write a string to utf-8 file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
