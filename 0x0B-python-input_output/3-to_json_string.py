#!/usr/bin/python3
"""
Contain to_json_string fundtion
"""

import json


def to_json_string(my_obj):
    """returns the JSON repre of an object (str)"""
    return json.dumps(my_obj)
