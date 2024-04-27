#!/usr/bin/python3
"""
-sends a request to the URL
-displays the value of the X-Request-Id in the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.headers
        print(header.get("X-Request-Id"))
