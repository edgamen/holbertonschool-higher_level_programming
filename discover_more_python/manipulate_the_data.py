""" This program parses the response from Github's API when requesting 
    the 30 most popular Python projects to a file into a JSON format and print it
"""
from urllib2 import Request, urlopen, URLError
import json

request_headers = {
    'User-Agent': 'Holberton School',
    'Authorization': 'token  3d59bbfb240064a050cb72476c091bd363e5267c'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
        response = urlopen(request)
        string = response.read()
        parsed = json.loads(string)
        for item in parsed["items"]:
                print item.get("full_name")
except URLError, e:
    print "Error code: ", e

