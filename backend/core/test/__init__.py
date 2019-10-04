from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestBase(APITestCase):

    def setUp(self):
        self.token = None

    @staticmethod
    def register_user(username, password):
        user = User.objects.create_user(username=username, password=password, email=username + '@gmail.com')
        user.set_password(password)
        user.save()
        return user

    def authenticate(self, username, password):
        result = self.client.post('/api/token/', {'username': username, 'password': password})
        self.token = None if result.status_code != 200 else result.data['access']
        return self.token

    def get(self, uri):
        return self.client.get('/api/v1/%s' % uri, HTTP_AUTHORIZATION='Bearer %s' % self.token)

    def post(self, uri, data):
        return self.client.post('/api/v1/%s' % uri, data, HTTP_AUTHORIZATION='Bearer %s' % self.token, format='json')
