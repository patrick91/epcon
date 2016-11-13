import os
import socket
import pytest

from tests.integration_tests.steps.page_steps import *  # noqa

from tests.liveserver_helper import DebugableLiveServer


@pytest.fixture
def selenium(selenium):
    socket.setdefaulttimeout(30)
    selenium.implicitly_wait(500)
    return selenium


@pytest.fixture(scope='session')
def live_server(request):
    """Run a live Django server in the background during tests
    The address the server is started from is taken from the
    --liveserver command line option or if this is not provided from
    the DJANGO_LIVE_TEST_SERVER_ADDRESS environment variable.  If
    neither is provided ``localhost:8081,8100-8200`` is used.  See the
    Django documentation for it's full syntax.
    NOTE: If the live server needs database access to handle a request
          your test will have to request database access.  Furthermore
          when the tests want to see data added by the live-server (or
          the other way around) transactional database access will be
          needed as data inside a transaction is not shared between
          the live server and test code.
          Static assets will be automatically served when
          ``django.contrib.staticfiles`` is available in INSTALLED_APPS.
    """
    import django

    addr = (request.config.getvalue('liveserver') or
            os.getenv('DJANGO_LIVE_TEST_SERVER_ADDRESS'))

    if addr and django.VERSION >= (1, 11) and ':' in addr:
        request.config.warn('D001', 'Specifying a live server port is not supported '
                            'in Django 1.11. This will be an error in a future '
                            'pytest-django release.')

    if not addr:
        if django.VERSION < (1, 11):
            addr = 'localhost:8081,8100-8200'
        else:
            addr = 'localhost'

    server = DebugableLiveServer(addr)
    request.addfinalizer(server.stop)
    return server
