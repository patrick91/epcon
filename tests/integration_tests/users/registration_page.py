from django.core.urlresolvers import reverse

from webium import BasePage, Find

from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    first_name = Find(by=By.ID, value='id_first_name')
    last_name = Find(by=By.ID, value='id_last_name')
    email = Find(by=By.ID, value='id_email')
    password1 = Find(by=By.ID, value='password1')
    password2 = Find(by=By.ID, value='password2')
    form = Find(by=By.XPATH, value='/html/body/div[1]/div/section/div/div[2]/div/form')

    def __init__(self, *args, **kwargs):
        super(RegistrationPage, self).__init__(*args, **kwargs)

        base_url = kwargs.pop('url', None)

        if base_url:
            self.url = base_url + reverse('assopy-new-account')
