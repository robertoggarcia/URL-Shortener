import factory

from core.factories.user import UserFactory
from core.models import Url


class UrlFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Url
    user = factory.SubFactory(UserFactory)
    url = factory.Sequence(lambda n: 'https://google.com/%d' % n)
