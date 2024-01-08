#!/usr/bin/python3
"""script that fetches github repo that was  committed """
from requests import get auth
from sys import argv


if __name__ == "__main__":
    try:
        repos = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repos)
        req = get(url)
        jsonO = req.json()
        for x in range(0, 10):
            print("{}: {}".format(jsonO[x].get("sha"), jsonO[x].get('commit')
                                  .get('author').get('name')))
    except Exception as e:
        pass
