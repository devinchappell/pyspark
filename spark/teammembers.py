"""
This module holds the TeamMembers class, used to manage Team Memberships
"""
from .sparkrequest import SparkRequest

class TeamMembers(object):
    """
    Used to interact with Spark Rooms
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, team_id, max_item=None):
        """
        List Memberships for all teams that the API User Belongs Too
        """
        req = SparkRequest(self._token)
        if bool(max_item):
            req.set_param('max', max_item)
        req.set_param('teamId', team_id)
        resp = req.get('team/memberships')
        return resp['items']

    def create(self, team_id, person_id=None, person_email=None, is_moderator=False):
        """
        Creates membership in room room_id
        YOU MUST SUPPLY EITHER PERSON_ID OR PERSON_EMAIL
        """
        if not bool(person_id) and not bool(person_email):
            raise ValueError("This module requires personId or personEmail")
        if bool(person_id) and bool(person_email):
            raise ValueError("Please provide personId OR personEmail, Not Both")
        if is_moderator:
            str_bool = 'true'
        else:
            str_bool = 'false'
        req = SparkRequest(self._token)
        req.set_data('teamId', team_id)
        req.set_data('isModerator', str_bool)
        if bool(person_id):
            req.set_data('personId', person_id)
        if bool(person_email):
            req.set_data('personEmail', person_email)
        resp = req.post('team/memberships')
        team_member_id = resp['id']
        return team_member_id

    def get_detail(self, team_member_id):
        """
        Returns a single Team Membership
        """
        req = SparkRequest(self._token)
        resp = req.get('team/memberships/' + team_member_id)
        return resp

    def update(self, team_member_id, is_moderator):
        """
        Updates a membership Entry. Used to set/unset moderator privs
        """
        req = SparkRequest(self._token)
        req.set_data('isModerator', is_moderator)
        req.put('team/memberships/' + team_member_id)
        if req.response_code == 200:
            return True
        return False

    def delete(self, team_member_id):
        """
        Used to remove team membership
        """
        req = SparkRequest(self._token)
        req.delete('team/memberships/' + team_member_id)
        if req.response_code == 204:
            return True
        return False 