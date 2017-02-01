from .people import People
from .rooms import Rooms

class SparkApi(object):

    def __init__(self, token):
        self._token = token
        self.people = People(self._token)
        self.rooms = Rooms(self._token)

    def set_token(self, token):
        self._token = token

    