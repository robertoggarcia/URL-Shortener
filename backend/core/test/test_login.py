from django.contrib.auth.models import User
from core.test import TestBase


class LoginTest(TestBase):

    def setUp(self):
        self.user = User.objects.create(username='admin', email='admin1@gmail.com')
        self.user.set_password('admin')
        self.user.save()

    def test_get_authenticate(self):
        result = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})

        assert result.status_code == 200
        assert result.data['access']
