#!/usr/bin/python3
"""
Contain load_from_json_file Function
"""

import json


def load_from_json_file(filename):
    """creating an Object from the "JSON file" """
    with open(filename, 'r', encoding='utf-8') as x:
        return json.load(x)
