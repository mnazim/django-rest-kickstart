from .common import *

DEBUG = True

SECRET_KEY = 'asdaksjdhaksjd kj12kj3h1k2j3h 1kj23h 1k2j3h 12kj3'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'developer',
        'PASSWORD': 'password'
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]
