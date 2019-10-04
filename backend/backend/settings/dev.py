from backend.settings.base import Base
from configurations import values
import os


class Dev(Base):
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = ['*']
    CORS_ORIGIN_ALLOW_ALL = True

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASES = values.DatabaseURLValue('postgres://postgres:postgres@localhost/fondeadora')

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
