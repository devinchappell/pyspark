"""
This module holds the Webhooks Class, used to manage Webhooks
"""
from .sparkrequest import SparkRequest

class Webhooks(object):
    """
    Used to interact with Webhooks
    """
    __module__ = 'spark'

    def __init__(self, token):
        self._token = token

    def get(self, max_item=None):
        """
        List all webhooks
        """
        req = SparkRequest(self._token)
        if bool(max_item):
            req.set_param('max', max_item)
        resp = req.get('webhooks')
        return resp['items']

    def get_detail(self, webhook_id):
        """
        Returns a single Webhook
        """
        req = SparkRequest(self._token)
        resp = req.get('webhooks/' + webhook_id)
        return resp

    def update(self, webhook_id, name, target_url):
        """
        Updates a webhook by id (webhook_id)
        Returns True if successful
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', target_url)
        req.put('webhooks/' + webhook_id)
        if req.response_code == 200:
            return True
        return False

    def delete(self, webhook_id):
        """
        Deletes a webhook
        """
        req = SparkRequest(self._token)


    def create_memberships_created(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone joins a room you're in
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'created')
        req.set_data('resource', 'memberships')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_memberships_updated(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone's permissions change in a room
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'updated')
        req.set_data('resource', 'memberships')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_memberships_deleted(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone is removed from a room
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'deleted')
        req.set_data('resource', 'memberships')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_messages_created(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone posts a message
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'created')
        req.set_data('resource', 'messages')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_messages_deleted(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone deletes a message
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'deleted')
        req.set_data('resource', 'messages')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_rooms_created(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone creates a room
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'created')
        req.set_data('resource', 'rooms')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id

    def create_rooms_updated(self, name, targeturl, w_filter=None, secret=None):
        """
        Create a listener for when someone changes a room
        """
        req = SparkRequest(self._token)
        req.set_data('name', name)
        req.set_data('targetUrl', targeturl)
        if bool(w_filter):
            req.set_data('filter', w_filter)
        if bool(secret):
            req.set_data('secret', secret)
        req.set_data('event', 'updated')
        req.set_data('resource', 'rooms')
        resp = req.post('webhooks')
        webhook_id = resp['id']
        return webhook_id
