#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL

status_code=$(curl -s -o /dev/null -w "%{http_code}\n" "$1")

if [ $status_code -eq 200 ];
then
    curl -s "$1"
fi
