from generators.email_generators import email_random
from utils.assertions import assert_url_contains
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from generators import email_generators
from generators import password_generators
import config
import pytest

@pytest.mark.e2e
@pytest.mark.regression
def test_registration_valid_data(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()