"""
This module holds the Rooms Class, used to manage rooms
"""
from .sparkrequest import SparkRequest

class Rooms(object):
    """
    Used to interact with Spark Rooms
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, team_id=None, max_item=None, room_type=None):
        """
        List rooms, with optional filters for type (can be direct or group),
        teams and a max item
        """
        req = SparkRequest(self._token)
        if bool(team_id):
            req.set_param('teamId', team_id)
        if bool(max_item):
            req.set_param('max', max_item)
        if bool(room_type):
            req.set_param('type', room_type)
        resp = req.get('rooms')
        return resp['items']

    def get_detail(self, room_id):
        """
        Return room details
        """
        req = SparkRequest(self._token)
        resp = req.get('rooms/' + room_id)
        return resp

    def create(self, title, team_id=None):
        """
        Creates a spark Room. Returns the room ID if Successful
        """
        req = SparkRequest(self._token)
        if bool(team_id):
            req.set_data('team_id', team_id)
        req.set_data('title', title)
        resp = req.post('rooms')
        room_id = resp['id']
        return room_id

    def delete(self, room_id):
        """
        Deletes a spark room. Returns True if successful, false if not
        """
        req = SparkRequest(self._token)
        req.delete('rooms/' + room_id)
        if req.response_code == 204:
            return True
        return False

    def update(self, room_id, title):
        """
        Updates the title of an existing Spark room. Returns True if successful
        """
        req = SparkRequest(self._token)
        req.set_data('title', title)
        req.put('rooms/' + room_id)
        if req.response_code == 200:
            return True
        return False

