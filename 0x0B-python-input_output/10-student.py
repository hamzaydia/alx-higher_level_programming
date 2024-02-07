#!/usr/bin/python3
""" Module of student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Constructor for new student """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """ Return dict for the student """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
