from pages.main_page import MainPage
import pytest

@pytest.mark.e2e
@pytest.mark.regression
def test_school_registration_valid_data(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.submit_school_registration()
    assert main_page.school_error() is False

def test_school_registration_invalid_postal_code(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_invalid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    assert main_page.assert_input_length() is True

def test_school_registration_invalid_nip(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_invalid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_letters_nip(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_invalid_letters_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_regon(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_invalid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_letters_regon(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_invalid_letters_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_special_email(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_special_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_no_domen_email(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_no_domen_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_double_at_email(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_double_at_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_invalid_without_at_email(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_without_at_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.click_on_voivodeship()
    main_page.choose_voivodeship()
    assert main_page.school_error() is not True

def test_school_registration_no_accepted_terms(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_gdpr()
    main_page.submit_school_registration()
    assert main_page.school_error() is not True

def test_school_registration_no_accepted_gdpr(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_valid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.submit_school_registration()
    assert main_page.school_error() is not True

def test_school_registration_invalid_contact_phone(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.fill_valid_school_name()
    main_page.fill_valid_school_street()
    main_page.fill_valid_school_building_number()
    main_page.fill_valid_school_postal_code()
    main_page.fill_valid_school_city()
    main_page.fill_valid_school_nip()
    main_page.fill_valid_school_regon()
    main_page.fill_valid_school_website()
    main_page.fill_valid_school_submitter_name()
    main_page.fill_valid_school_submitter_role()
    main_page.fill_invalid_school_contact_phone()
    main_page.fill_valid_school_contact_email()
    main_page.accept_school_terms()
    main_page.accept_school_gdpr()
    main_page.submit_school_registration()
    assert main_page.school_error() is not True

def test_school_registration_empty_fields(driver):
    main_page = MainPage(driver)

    main_page.go_to_school_registration()
    main_page.submit_school_registration()
    assert main_page.school_error() is not True