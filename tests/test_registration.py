from generators.email_generators import email_random
from pages import registration_page
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
    assert registration_page.get_success_message() is not None

def test_registration_special_email(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_special_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_success_message() is not None

def test_registration_no_domen_email(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_no_domen_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_double_at_email(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_double_at_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_without_at_email(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_without_at_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_with_too_short_password(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_too_short_password()
    registration_page.fill_repeat_too_short_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_with_not_same_password(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_not_same_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_with_invalid_grade(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_invalid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_without_checkboxes(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.submit_registration()
    assert registration_page.checkbox_error_message is not None

def test_registration_with_empty_fields(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_with_too_long_password(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_valid_email()
    registration_page.fill_username()
    registration_page.fill_too_long_password()
    registration_page.fill_repeat_too_long_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.get_error_message()

def test_registration_with_existing_email(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)

    main_page.go_to_registration()

    registration_page.fill_existing_email()
    registration_page.fill_username()
    registration_page.fill_valid_password()
    registration_page.fill_repeat_valid_password()
    registration_page.fill_valid_grade()
    registration_page.fill_terms_checkbox()
    registration_page.fill_gdpr_checkbox()
    registration_page.submit_registration()
    assert registration_page.register_error_message is not None