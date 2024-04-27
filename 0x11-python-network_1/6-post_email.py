#!/usr/bin/python3
"""
-takes in a URL and an email address
-sends a POST request to the URL with the email as a parameter
-displays the body of the response
"""
if __name__ == "__main__":
    import requests
    import sys

    values = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=values)
    print(r.text)
