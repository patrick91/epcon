import socket
import pytest

from tests.integration_tests.steps.page_steps import *  # noqa


@pytest.fixture
def selenium(selenium):
    socket.setdefaulttimeout(30)
    selenium.implicitly_wait(500)
    return selenium
