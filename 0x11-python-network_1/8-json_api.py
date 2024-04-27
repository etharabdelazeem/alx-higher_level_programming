#!/usr/bin/python3
"""
-Takes in a letter and sends a POST request to a URL
-If the response body is properly JSON formatted and not empty:
    Displays the id and name
-Otherwise:
    Displays Not a valid JSON if the JSON is invalid
    Displays No result if the JSON is empty
"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        l = ""
    else:
        l = sys.argv[1]
    values = {'q': l}
    r = requests.post("http://0.0.0.0:5000/search_user", data=values)
    try:
        r = r.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
