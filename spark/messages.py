"""
This module holds the Messages Class, used to manage messages
"""
import datetime
from .sparkrequest import SparkRequest

class Messages(object):
    """
    Used to generate and manipulate messages
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, r_id, mentioned=None, before_date=None, before_msg=None, max=None):
        """
        Retrive all messages for a given room (r_id)
        """
        req = SparkRequest
        req.set_param('roomId', r_id)
        if bool(mentioned):
            req.set_param('mentionedPeople', mentioned)
        if bool(before_date):
            iso_date = datetime.datetime(before_date).isoformat
            

