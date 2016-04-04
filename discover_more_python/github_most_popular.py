""" This program prints the response from Github's API when requesting 
    the 30 most popular Python projects
"""
from urllib2 import Request, urlopen, URLError

request_headers = {
            'User-Agent': 'Holberton School',
            'Authorization': 'token ae6b5eaf4971c9e50adafdb86513c15df7de6fbb'
        }

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=request_headers)

try:
        response = urlopen(request)
        string = response.read()
        print string
except URLError, e:
    print "Error code: ", e
