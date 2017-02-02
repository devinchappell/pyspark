"""
This module contains the SparkRequest Class, which is used to handle HTTP Requests to the Spark API
"""

import json
import sys
import requests

class SparkRequest(object):
    """
    This class is used as a shim between the Spark API Modules and the Requests Libraries
    We preload the token variable from the caller, and define empty dicts for the payload
    (POST Data), params (Query Params), and headers

    The self._req object is used to hold the Request object, in case we need to expose the
    response code to the caller. Work in progress
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._req = None
        self._token = token
        self.params = {}
        self.payload = {}
        self.headers = {"Content-Type": "application/json"}
        self.url = "https://api.ciscospark.com/v1/"
        self.set_header("Authorization", "Bearer " + token)

    def response_code(self):
        """
        Used to present HTTP Reponse code as requested
        """
        return self._req.status_code

    def set_header(self, header, value):
        """
        We use this to add headers (mainly the auth bearer token) as needed.
        """
        self.headers[header] = value

    def rem_header(self, header):
        """
        used to remove established headers. Not used yet, but defined just-in-case
        """
        if header in self.headers:
            del self.headers[header]

    def set_param(self, param, value):
        """
        Used to set query parameters for GET Operations
        """
        self.params[param] = value

    def rem_param(self, param):
        """
        Used to remove query parameters already set
        """
        if param in self.params:
            del self.params[param]

    def set_data(self, key, value):
        """
        POST Data is delivered in JSON, so we store it in the
        request object as a Dict, and then json.dumps it in the request object
        """
        self.payload[key] = value

    def rem_data(self, key):
        """
        to remove POST data from a request
        """
        if key in self.payload:
            del self.payload

    def get(self, api_url):
        """
        Send the request data in a GET
        """
        r_url = self.url + api_url
        try:
            if bool(self.params): #Only send query parameters if defined
                self._req = requests.get(r_url, params=self.params, headers=self.headers)
            else:
                self._req = requests.get(r_url, headers=self.headers)
            self._req.raise_for_status()
            return json.loads(self._req.content)
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(self._req.content)
            sys.exit(1)

    def post(self, api_url):
        """
        Send the request data in a POST
        """
        r_url = self.url + api_url
        try:
            self._req = requests.post(r_url, headers=self.headers, data=json.dumps(self.payload))
            self._req.raise_for_status()
            return json.loads(self._req.content)
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(self._req.content)
            sys.exit(1)

    def put(self, api_url):
        """
        Send the request as a PUT
        """
        r_url = self.url + api_url
        try:
            self._req = requests.put(r_url, headers=self.headers, data=json.dumps(self.payload))
            self._req.raise_for_status()
            return json.loads(self._req.content)
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(self._req.content)
            sys.exit(1)

    def delete(self, api_url):
        """
        Send a DELETE
        """
        r_url = self.url + api_url
        try:
            self._req = requests.delete(r_url, headers=self.headers)
            self._req.raise_for_status()
            return None
        except requests.exceptions.HTTPError as err:
            print err
            print json.loads(self._req.content)
            sys.exit(1)
    