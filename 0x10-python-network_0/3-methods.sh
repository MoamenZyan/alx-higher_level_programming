#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS 0.0.0.0:5000 | grep ^Allow | cut -d ':' -f 2 | cut -c 2-
