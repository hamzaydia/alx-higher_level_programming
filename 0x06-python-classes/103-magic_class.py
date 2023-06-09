#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        """Magic class init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of a circle"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """Circumference of a circle"""
        return (math.pi * self.__radius * 2)
