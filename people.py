from .sparkrequest import SparkRequest

class People(object):
    __module__ = 'Spark'

    def __init__(self, token):
        self._token = token

    def get(self, maxItem=None):
        r = SparkRequest(self._token)
        if bool(maxItem):
            r.setParam('max', maxItem)
        resp = r.get('people')
        return resp

    def getByEmail(self, email):
        r = SparkRequest(self._token)
        r.setParam('email', email)
        resp = r.get('people')
        return resp

    def getByDisplayName(self, displayName):
        r = SparkRequest(self._token)
        r.setParam('displayName', displayName)
        resp = r.get('people')
        return resp

    def getDetail(self, userId):
        r = SparkRequest(self._token)
        resp = r.get('people/' + userId)
        return resp

    def getDetailByEmail(self, email):
        rSet = self.getByEmail(email)
        if len(rSet['items']) > 0:
            userId = rSet['items'][0]['id']
            return self.getDetail(userId)
        else:
            return None

    def getMe(self):
        r = SparkRequest(self._token)
        resp = r.get('people/me')
        return resp