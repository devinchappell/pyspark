"""
This module contains the People Class, which is used to manipulate People in
Spark
"""

from .sparkrequest import SparkRequest

class People(object):
    """
    Used to work with People Objects
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, max_item=None):
        """
        Returns a list of all users in the org used by the requestor
        NEED ADMIN PRIVILEGES TO WORK
        """
        req = SparkRequest(self._token)
        if bool(max_item):
            req.set_param('max', max_item)
        resp = req.get('people')
        return resp

    def get_by_email(self, email):
        """
        Returns a Spark User based on email address
        """
        req = SparkRequest(self._token)
        req.set_param('email', email)
        resp = req.get('people')
        return resp

    def get_by_display_name(self, display_name):
        """
        Searches for Spark Users based on Display Name
        Doesnt seem really reliable, but it's implemented on the API, so...
        """
        req = SparkRequest(self._token)
        req.set_param('displayName', display_name)
        resp = req.get('people')
        return resp

    def get_detail(self, user_id):
        """
        Give a User ID, return all user details
        """
        req = SparkRequest(self._token)
        resp = req.get('people/' + user_id)
        return resp

    def get_detail_by_email(self, email):
        """
        Just a handy function to pass an email address (always unique
        because spark prevents duplicate emails) and return details
        """
        r_set = self.get_by_email(email)
        if len(r_set['items']) > 0:
            user_id = r_set['items'][0]['id']
            return self.get_detail(user_id)
        else:
            return None

    def get_me(self):
        """
        Get Account details of the account that owns the auth token
        """
        req = SparkRequest(self._token)
        resp = req.get('people/me')
        return resp
