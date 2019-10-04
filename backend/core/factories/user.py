import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda a: '{0}@gmail.com'.format(a.username).lower())

