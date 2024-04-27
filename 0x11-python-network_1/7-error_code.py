#!/usr/bin/python3
"""
-sends a request to the URL
-displays the body of the response
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    status_code = r.status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        print(r.text)
