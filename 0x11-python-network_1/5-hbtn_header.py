#!/usr/bin/python3
"""
Accepts  a URL, sends a request to the URL and shows the value of the
variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
