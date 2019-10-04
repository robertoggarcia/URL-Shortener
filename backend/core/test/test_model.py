from django.contrib.auth.models import User

from core.factories.url import UrlFactory
from core.factories.user import UserFactory
from core.models import Url
from core.test import TestBase


class TestUrlModel(TestBase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_url(self):
        UrlFactory(user=self.user)

        url = Url.objects.filter(user=self.user).last()

        assert url.short_url == url.id
        assert url.expire_at
