#!/usr/bin/python3
""" Contains add_attribute Function"""


def add_attribute(obj, name, value):
    """This add attributes"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
