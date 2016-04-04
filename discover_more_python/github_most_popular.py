""" This program prints the response from Github's API when requesting 
    the 30 most popular Python projects
"""
from urllib2 import Request, urlopen, URLError

request_headers = {
    'User-Agent': 'Holberton School',
    'Authorization': 'token  3d59bbfb240064a050cb72476c091bd363e5267c'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
        response = urlopen(request)
        string = response.read()
        print string
except URLError, e:
    print "Error code: ", e
