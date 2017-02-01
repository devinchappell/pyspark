import requests
import json
import sys

class SparkRequest(object):
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token
        self.params = {}
        self.payload = {}
        self.headers = {"Content-Type": "application/json"}
        self.url = "https://api.ciscospark.com/v1/"
        self.setHeader("Authorization", "Bearer " + token)

    def setHeader(self, header, value):
        self.headers[header] = value

    def remHeader(self, header):
        if header in self.headers:
            del self.headers[header]
    
    def setParam(self, param, value):
        self.params[param] = value

    def remParam(self, param):
        if param in self.params:
            del self.params[param]

    def setData(self, key, value):
        self.payload[key] = value

    def remData(self, key):
        if key in self.payload:
            del self.payload

    def get(self, ApiUrl):
        r_url = self.url + ApiUrl
        try:
            if bool(self.params):
                r = requests.get(r_url, params=self.params, headers=self.headers)
            else:
                r = requests.get(r_url, headers=self.headers)
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(r.content)
            sys.exit(1)

    def post(self, ApiUrl):
        r_url = self.url + ApiUrl
        try:
            r = requests.post(r_url, headers=self.headers, data=self.payload)
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(r.content)
            sys.exit(1)

    