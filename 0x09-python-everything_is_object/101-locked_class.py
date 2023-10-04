#!/usr/bin/python3
"""
    Module for `LockedClass`
"""


class LockedClass:
    """
        LockedClass that wont allow any instance attributes that's not
        for `first_name`.
    """

    def __setattr__(self, name, value):
        """
            Override  method `setattr` to prevent instance
            attributes that's not `first_name` to be add to the instance's dict.
            Args:
                name (:obj:`str`): Name of the proposed attribute.
                value (any): value  assigned to proposed attribute.
        """
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")

    def __getattribute__(self, name):
        """
            Override the reserved method `getattr` to preven retrieval of any
            attributes, including instance's dict.
            Args:
                name (:obj:`str`): A string.
        """
        if name == "__dict__":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")
