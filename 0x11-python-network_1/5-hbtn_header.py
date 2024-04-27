#!/usr/bin/python3
"""
-sends a request to the URL
-displays the value of the X-Request-Id in the response
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    header = r.headers
    print(header.get("X-Request-Id"))
