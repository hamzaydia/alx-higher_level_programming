#!/usr/bin/python3
""" Module of Student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Constructor for new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dict for new student """
        return self.__dict__
