#!/usr/bin/python3
"""
Contain append_wrtie function
"""


def append_write(filename="", text=""):
    """returnsnum of char added to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
