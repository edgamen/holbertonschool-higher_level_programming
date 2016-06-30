import threading
import requests
import json

class IPThread(threading.Thread):

    def __init__(self, ip, callback):
        if type(ip) is not str:
            raise Exception("IP address passed is not str")
        self.ip = ip
        self.callback = callback
        threading.Thread.__init__(self)

    ''' make a request to an API to access information about IP '''
    def run(self):
        print "Search: %s" % self.ip
        url = 'https://api.ip2country.info/ip?' + self.ip
        json_str = requests.get(url).text
        ''' print json_str '''

        country_name = self.__return_country_name(json_str)
        self.callback(country_name)
        print "countryName: %s" % country_name

    ''' parse json string and return value of countryName key '''
    def __return_country_name(self, json_str):
        array = json.loads(json_str)
        return array['countryName']
