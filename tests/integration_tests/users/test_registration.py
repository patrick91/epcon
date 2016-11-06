from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from webium.driver import close_driver

from tests.integration_tests.users.registration_page import RegistrationPage


class TestUsersCase(StaticLiveServerTestCase):
    def tearDown(self):
        close_driver()

    def test_user_can_register_using_email_and_password(self):
        page = RegistrationPage(url=self.live_server_url)
        page.open()

        page.first_name.send_keys('Justin')
        page.last_name.send_keys('Pound')
        page.email.send_keys('justing.pound@yahoo.nl')
        page.password1.send_keys('my-is_secure')
        page.password2.send_keys('my-is_secure')

        page.form.submit()
