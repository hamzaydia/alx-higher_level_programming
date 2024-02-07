#!/usr/bin/python3
""" Module for file reader """


def read_file(filename=""):
    """ Read and print content of file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
