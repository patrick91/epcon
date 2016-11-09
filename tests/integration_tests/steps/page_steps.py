from pytest_bdd import given

from tests.integration_tests.users.registration_page import RegistrationPage


AVAILABLE_PAGES = {
    'registration': RegistrationPage,
}


@given('the user is on the {page} page')
def go_to_page(context, page, live_server, selenium):
    if page not in AVAILABLE_PAGES:
        # Warn about the invalid page?
        raise KeyError('Page {} is not a valid page. Valid pages: {}'.format(page, AVAILABLE_PAGES))

    page_cls = AVAILABLE_PAGES[page]
    context.page = page_cls(base_url=live_server.url, selenium=selenium)
