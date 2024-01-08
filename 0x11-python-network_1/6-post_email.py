#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':

    newV = {'email': sys.argv[2]}
    reqs = requests.post(sys.argv[1], newV)
    print(reqs.text)
