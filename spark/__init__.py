from .people import People
from .rooms import Rooms
from .memberships import Memberships
from .messages import Messages
from .teams import Teams
from .teammembers import TeamMembers
from .webhooks import Webhooks


class SparkApi(object):

    def __init__(self, token):
        self._token = token
        self.people = People(self._token)
        self.rooms = Rooms(self._token)
        self.memberships = Memberships(self._token)
        self.messages = Messages(self._token)
        self.teams = Teams(self._token)
        self.teammembers = TeamMembers(self._token)
        self.webhooks = Webhooks(self._token)

    def set_token(self, token):
        self._token = token

    