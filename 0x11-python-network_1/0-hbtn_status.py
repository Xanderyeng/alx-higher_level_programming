#!/usr/bin/python3
"""
 script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    answer = 'Body response:\n\t- type: {}\n\t- content: {}\
\n\t- utf8 content: {}'.format(type(html), html, html.decode('UTF-8'))
    print(answer)