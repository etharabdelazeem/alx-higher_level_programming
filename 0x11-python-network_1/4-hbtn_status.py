#!/usr/bin/python3
"""
a Python script that fetches a url and displays the response
"""
if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
