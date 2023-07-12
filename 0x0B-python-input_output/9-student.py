#!/usr/bin/python3
"""Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Student class init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary of Student"""
        return self.__dict__
