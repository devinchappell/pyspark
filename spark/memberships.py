"""
This module holds the Membership Class, used to manage rooms
"""
from .sparkrequest import SparkRequest

class Memberships(object):
    """
    Memberships are how Spark handles room members
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, r_id=None, p_id=None, p_email=None, max=None):
        """
        Returns a JSON item containing all membership entries
        r_id = roomId, p_id = personId, p_email = personEmail
        """
        req = SparkRequest(self._token)
        if bool(r_id):
            req.set_param('roomId', r_id)
        if bool(p_id):
            req.set_param('personId', p_id)
        if bool(p_email):
            req.set_param('personEmail', p_email)
        if bool(max):
            req.set_param('max', max)
        resp = req.get('memberships')
        return resp['items']

    def create(self, r_id, p_id=None, p_email=None, mod=False):
        """
        Creates a membership (adds user to room)
        Account used by API must be a member
        r_id = roomId, p_id = personId, p_email = personEmail
        mod = Moderator. Returns membershipId if successful
        """
        if not bool(p_id) and not bool(p_email):
            raise ValueError("This module requires personId or personEmail")
        req = SparkRequest(self._token)
        if bool(r_id):
            req.set_data('roomId', r_id)
        if bool(p_id):
            req.set_data('personId', p_id)
        if bool(p_email):
            req.set_data('personEmail', p_email)
        if bool(mod):
            req.set_data('isModerator', 'false')
        else:
            req.set_data('isModerator', 'true')
        resp = req.post('memberships')
        membership_id = resp['id']
        return membership_id

    def get_detail(self, member_id):
        """
        Returns a single membership instance
        """
        req = SparkRequest(self._token)
        resp = req.get('memberships/' + member_id)
        return resp

    def update(self, member_id, moderator):
        """
        Used to enable/disable moderator privileges
        Moderator is a boolean
        """
        req = SparkRequest(self._token)
        if moderator:
            str_mod = 'true'
        else:
            str_mod = 'false'
        req.set_data('isModerator', str_mod)
        req.put('memberships/' + member_id)
        if req.response_code == 200:
            return True
        return False

    def delete(self, member_id):
        """
        Deletes a Membership and Returns True if successful
        """
        req = SparkRequest(self._token)
        req.delete('memberships/' + member_id)
        if req.response_code == 204:
            return True
        return False
        