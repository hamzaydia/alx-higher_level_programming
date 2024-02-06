#!/usr/bin/python3
""" Module of `Square` class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Constructor method """
        super().integer_validator("size", size)
        super().__init__(size, size)
