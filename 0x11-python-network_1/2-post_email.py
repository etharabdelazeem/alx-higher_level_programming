#!/usr/bin/python3
"""
-sends a request to the URL
-displays the value of the X-Request-Id in the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
