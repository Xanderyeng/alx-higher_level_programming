#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    answer = 'Body response:\n\t- type: {}\n\t- content: {}'\
        .format(type(r.text), r.text)
    print(answer)