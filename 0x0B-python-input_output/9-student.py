#!/usr/bin/python3
"""
Contains Student Class
"""


class Student:
    """Repre of student"""
    def __init__(self, first_name, last_name, age):
        """Initializing the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict repre of a Student instance"""
        return self.__dict__
