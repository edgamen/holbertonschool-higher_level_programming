""" This program parses the response from Github's API when requesting 
    the 30 most popular Python projects to a file into a JSON format and
    prints the name of each project
"""
from urllib2 import Request, urlopen, URLError
import json

request_headers = {
    'User-Agent': 'Holberton School',
    'Authorization': 'token ae6b5eaf4971c9e50adafdb86513c15df7de6fbb'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=request_headers)

try:
        response = urlopen(request)
        string = response.read()
        parsed = json.loads(string)
        for item in parsed["items"]:
                print item.get("full_name")
except URLError, e:
    print "Error code: ", e

