import socket
import pytest


@pytest.fixture
def selenium(selenium):
    socket.setdefaulttimeout(30)
    selenium.implicitly_wait(500)
    return selenium
