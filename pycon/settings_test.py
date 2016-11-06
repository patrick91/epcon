from pycon.settings import *  # noqa

import webium.settings

from selenium.webdriver import Chrome

DEBUG = True

SECRET_KEY = "your-secret-key"

RAVEN_CONFIG = {
    'dsn': '',
}

webium.settings.driver_class = Chrome
webium.settings.implicit_timeout = 50000
webium.settings.wait_timeout = 50000
