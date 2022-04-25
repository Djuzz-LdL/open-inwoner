from django.conf import settings
from django.contrib.sessions.backends.cache import SessionStore as BaseSessionStore

from open_inwoner.accounts.models import User

from .base import SplitSessionAge


class SessionStore(SplitSessionAge, BaseSessionStore):
    pass
