#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST
request to the passed URL and
displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    newV = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(newV).encode()
    reqs = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqs) as response:
        value = response.read().decode('utf8')
    print(value)
