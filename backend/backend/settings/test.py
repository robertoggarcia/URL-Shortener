from .dev import Dev
from configurations import values


class Test(Dev):
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = ['*']

