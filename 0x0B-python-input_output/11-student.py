#!/usr/bin/python3
""" Module for student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Constructor for new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dict of the student """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace student from JSON """
        for k, v in json.items():
            setattr(self, k, v)
