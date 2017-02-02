"""
This module holds the Teams Class, used to manage Teams
"""

from .sparkrequest import SparkRequest

class Teams(object):
    """
    Used to generate and manipulate messages
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, max_req=None):
        """
        Retrieve all teams that the user belongs to
        """
        req = SparkRequest(self._token)
        if bool(max_req):
            req.set_param('max', max_req)
        resp = req.get('teams')
        return resp['items']

    def create(self, name):
        """
        Create a new Team
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        resp = req.post('teams')
        team_id = resp['id']
        return team_id

    def get_detail(self, team_id):
        """
        Get a single team
        """
        req = SparkRequest(self._token)
        resp = req.get('teams/' + team_id)
        return resp

    def update(self, team_id, name):
        """
        Update the team with the given ID to the given name
        Returns True if Successful
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.put('teams/' + team_id)
        if req.response_code == 200:
            return True
        return False

    def delete(self, team_id):
        """
        Deletes the team with the id given
        Returns True if successful
        """
        req = SparkRequest(self._token)
        req.delete('teams/' + team_id)
        if req.response_code == 204:
            return True
        return False
        

    