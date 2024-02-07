#!/usr/bin/python3
""" Module to write file """


def write_file(filename="", text=""):
    """Write a string to a text file
    Returns:
        Number of chars """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
