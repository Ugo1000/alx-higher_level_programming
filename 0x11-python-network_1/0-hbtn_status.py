#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


# if __name__ == "__main__":
#     request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
#     with urllib.request.urlopen(request) as response:
#         body = response.read()
#         print("Body response:")
#         print("\t- type: {}".format(type(body)))
#         print("\t- content: {}".format(body))
#         print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read().decode("utf-8")
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
