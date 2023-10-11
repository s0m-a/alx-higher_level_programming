#!/usr/bin/python3
""" Student to JSON """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ gets a dict repre of a Student instance """
        if attrs is None:
            return (self.__dict__)
        else:
            dic = {}
            for n in attrs:
                if hasattr(self, n):
                    dic[n] = getattr(self, n)
            return (dic)

    def reload_from_json(self, json):
        """ Replace attributes of the Student instance"""
        save = vars(self)
        for key, value in json.items():
            save[key] = value
