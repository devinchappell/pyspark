from .sparkrequest import SparkRequest

class Rooms(object):
    __module__ = 'spark'

    def __init__(self, token):
       self._token = token

    def get(self, teamId=None, maxItem=None, roomType=None):
        r = SparkRequest(self._token)
        if bool(teamId):
            r.setParam('teamId', teamId)
        if bool(maxItem):
            r.setParam('max', maxItem)
        if bool(roomType):
            r.setParam('type', roomType)
        resp = r.get('rooms')
        return resp

    def getDetail(self, roomId):
        r = SparkRequest(self._token)
        resp = r.get('rooms/' + roomId)
        return resp

    def create(self, title, teamId=None):
        r = SparkRequest(self._token)
        
        if bool(teamId):
            r.setData('teamId', teamId)
        r.setData('title', title)
        resp = r.post('rooms')
        return resp
