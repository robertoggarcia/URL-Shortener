from .base import Base
from configurations import values
import os


class Deploy(Base):
    DEBUG = values.BooleanValue(False)
    ALLOWED_HOSTS = ['.robggarcia.tech']
    CORS_ORIGIN_REGEX_WHITELIST = [
        r"^*://*.robggarcia.tech:.*",
    ]

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASES = values.DatabaseURLValue('postgres://postgres:postgres@localhost/fondeadora')

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
