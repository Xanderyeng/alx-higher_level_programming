#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep Allow | cut -d ":" -f2 | cut -c 2-
