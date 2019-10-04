from django.http import HttpRequest

from core.factories.url import UrlFactory
from core.factories.user import UserFactory
from core.models import Url
from core.test import TestBase
from core.views import get_url


class TestUrlViewSet(TestBase):

    def setUp(self):
        self.user = self.register_user('admin', 'admin')
        self.authenticate('admin', 'admin')
        self.url = UrlFactory(user=self.user)

    def test_post_url(self):
        data = {
            'url': 'google.com',
            'user': str(self.user.id)
        }

        response = self.post('urls', data)

        urls = Url.objects.filter(url='google.com', user=self.user).count()

        assert response.status_code == 201
        assert urls == 1

    def test_get_url(self):
        response = self.get('urls')

        assert len(response.data) != 0

    def test_get_url_query(self):
        query = '?url={0}&user={1}'.format(self.url.url, str(self.user.id))

        response = self.get('urls', query)

        assert len(response.data) == 1

    def test_get_method(self):
        request = HttpRequest()
        request.method = 'GET'
        response = get_url(request, self.url.id)

        assert response.status_code == 302

    def test_url_get_view(self):
        response = self.client.get('/%s' % self.url.id)

        assert response.status_code == 301
        assert self.url.id in response.url
