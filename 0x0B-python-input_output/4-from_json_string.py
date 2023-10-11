#!/usr/bin/python3
"""
Contain from_json_string Function
"""

import json


def from_json_string(my_str):
    """returns an object repre by a JSON str"""
    return json.loads(my_str)
