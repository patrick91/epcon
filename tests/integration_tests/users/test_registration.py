from tests.integration_tests.users.registration_page import RegistrationPage


def test_user_can_register_using_email_and_password(live_server, selenium):
    page = RegistrationPage(base_url=live_server.url, selenium=selenium)
    page.open()

    page.first_name.send_keys('Justin')
    page.last_name.send_keys('Pound')
    page.email.send_keys('justing.pound@yahoo.nl')
    page.password1.send_keys('my-is_secure')
    page.password2.send_keys('my-is_secure')

    page.form.submit()
