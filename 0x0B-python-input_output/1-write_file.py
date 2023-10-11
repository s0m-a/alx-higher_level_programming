#!/usr/bin/python3
"""
Contain wrtie_file Function"
"""


def write_file(filename="", text=""):
    """returns num of char written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
