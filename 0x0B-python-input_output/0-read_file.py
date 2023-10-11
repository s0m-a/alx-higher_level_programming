#!/usr/bin/python3
"""
Contain read_file Function
"""


def read_file(filename=""):
    """""reads a text file and prints it's stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
