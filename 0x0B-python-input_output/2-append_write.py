#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """Append string to end of utf-8 file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
