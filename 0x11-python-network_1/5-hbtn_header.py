#!/usr/bin/python3

"""Sends a request to the URL."""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
