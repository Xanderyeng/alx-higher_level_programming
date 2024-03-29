#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ''}
    req = requests.post(url, q)
    try:
        rqjson = req.json()
        if len(rqjson) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(rqjson['id'], rqjson['name']))
    except:
        print('Not a valid JSON')