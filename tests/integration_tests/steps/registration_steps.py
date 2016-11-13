from pytest_bdd import given, when, then, parsers


@given(parsers.parse('that the user has filled the registration form with'))
def fill_registration_form(get_page, datatable):
    for field in datatable:
        field_name = field[0]
        value = field[1]

        getattr(get_page, field_name).send_keys(value)


@when('he submits the form')
def form_submit(get_page):
    raise NotImplementedError(u'STEP: When he submits the form')


@then('he should have an account with those information')
def account_data_check(get_page):
    raise NotImplementedError(u'STEP: Then he should have an account with those information')
