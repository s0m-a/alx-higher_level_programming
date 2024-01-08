#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable in the header
"""
import sys
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.info()
    print(value['X-Request-Id'])
