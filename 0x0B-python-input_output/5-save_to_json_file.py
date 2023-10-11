#!/usr/bin/python3
"""
Contains save_to_json_file Function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to text file, using JSON repre"""
    with open(filename, 'w', encoding='utf-8') as x:
        json.dump(my_obj, x)
