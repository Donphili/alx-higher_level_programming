#!/usr/bin/python3
"""
Desc: This module contains one class; Student
"""


class Student:
    """
    Reoresentation of the class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__
