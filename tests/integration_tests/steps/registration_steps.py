from pytest_bdd import given, when, then


@given('that the user has filled the registration form with')
def fill_registration_form(context):
    raise NotImplementedError(u'STEP: Given that the user has filled the registration form with')


@when('he submits the form')
def form_submit(context):
    raise NotImplementedError(u'STEP: When he submits the form')


@then('he should have an account with those information')
def account_data_check(context):
    raise NotImplementedError(u'STEP: Then he should have an account with those information')
