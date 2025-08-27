from pages.main_page import MainPage
from conftest import *

def test_send_valid_suggestion(driver):
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    main_page.valid_suggestion_message()
    main_page.send_suggestion()
    assert main_page.get_suggestions_success_message() is not None

def test_send_invalid_suggestion(driver):
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    main_page.invalid_suggestion_message()
    main_page.get_real_length()
    assert main_page.is_pasted_fully() is True

def test_send_empty_suggestion(driver):
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    main_page.send_suggestion()
    assert main_page.get_suggestions_error_message() is not None