#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses
the Github API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/user"

    req = requests.get(url, auth=(user, pwd))
    reqJsonRep = req.json()

    print(reqJsonRep.get("id", "None"))
