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

    def get(self, r_id, max_req=None):
        """
        Retrieve all messages for a given room (r_id)
        """
        req = SparkRequest(self._token)
        req.set_param('roomId', r_id)
        if bool(max_req):
            req.set_param('max', max_req)
        resp = req.get('messages')
        return resp['items']

    def get_before_date(self, r_id, msg_date, max_req=None):
        """
        retrieve all messages in a room before given date msg_date
        """
        req = SparkRequest(self._token)
        if bool(max_req):
            req.set_param('max', max_req)
        req.set_param('roomId', r_id)
        req.set_param('before', msg_date.isoformat())
        resp = req.get('messages')
        return resp['items']

    def get_before_msg(self, r_id, msg, max_req=None):
        """
        retrieve all messages in a room before given message (msg)
        """
        req = SparkRequest(self._token)
        if bool(max_req):
            req.set_param('max', max_req)
        req.set_param('roomId', r_id)
        req.set_param('beforeMessage', msg)
        resp = req.get('messages')
        return resp['items']

    def get_detail(self, msg_id):
        """
        Retrieve a single message
        """
        req = SparkRequest(self._token)
        resp = req.get('messages/' + msg_id)
        return resp

    def create_in_room(self, r_id, text, files=None):
        """
        Posts a message to a Spark room
        """
        req = SparkRequest(self._token)
        if bool(files):
            req.set_data('files', files)
        req.set_data('roomId', r_id)
        req.set_data('text', text)
        resp = req.post('messages')
        msg_id = resp['id']
        return msg_id

    def create_direct(self, text, p_id=None, p_email=None, files=None):
        """
        Creates a direct message to a person by id (p_id) or email (p_email)
        """
        if not bool(p_id) and not bool(p_email):
            raise ValueError("This module requires personId or personEmail")
        if bool(p_id) and bool(p_email):
            raise ValueError("This module only allows one of PersonId or PersonEmail to be defined")
        req = SparkRequest(self._token)
        if bool(files):
            req.set_data('files', files)
        if bool(p_id):
            req.set_data('toPersonId', p_id)
        if bool(p_email):
            req.set_data('toPersonEmail', p_email)
        req.set_data('text', text)
        resp = req.post('messages')
        msg_id = resp['id']
        return msg_id

    def delete(self, msg_id):
        """
        Deletes a Message
        Returns True if successful
        """
        req = SparkRequest(self._token)
        req.delete('messages/' + msg_id)
        if req.response_code == 204:
            return True
        return False

        