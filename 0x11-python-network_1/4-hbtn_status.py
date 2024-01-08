#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    resq = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format((type(resq.text))))
    print("\t- content: {}".format(resq.text))
