from conftest import *
from pages.suggestions_page import SuggestionsPage


def test_send_valid_suggestion(driver):
    suggestions_page = SuggestionsPage(driver)
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    suggestions_page.valid_suggestion_message()
    suggestions_page.send_suggestion()
    assert suggestions_page.get_suggestions_success_message() is not None

def test_send_invalid_suggestion(driver):
    suggestions_page = SuggestionsPage(driver)
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    suggestions_page.invalid_suggestion_message()
    suggestions_page.get_real_length()
    assert suggestions_page.is_pasted_fully() is True

def test_send_empty_suggestion(driver):
    suggestions_page = SuggestionsPage(driver)
    main_page = MainPage(driver)

    main_page.go_to_suggestions()
    suggestions_page.send_suggestion()
    assert suggestions_page.get_suggestions_error_message() is not None