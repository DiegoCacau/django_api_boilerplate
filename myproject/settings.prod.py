try:
    from .base import *  # noqa
except ImportError:
    pass

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
    'localhost'
)

DEBUG = False

sentry_sdk.init(
    dsn=config('SENTRY_DNS'),
    integrations=[DjangoIntegration()]
)

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True