#!/usr/bin/python3
""" Module to append to a file """


def append_write(filename="", text=""):
    """Append a string to the end of a file
    Returns: Number of chars """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
