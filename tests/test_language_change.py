from conftest import *
from pages.language_change_page import LanguageChangePage


def test_language_change_to_english(driver):
    main_page = MainPage(driver)
    language_change_page = LanguageChangePage(driver)

    main_page.go_to_language()
    language_change_page.change_lang_to_english()
    assert language_change_page.verify_english_language_change()

def test_language_change_to_ukranian(driver):
    main_page = MainPage(driver)
    language_change_page = LanguageChangePage(driver)

    main_page.go_to_language()
    language_change_page.change_lang_to_ukranian()
    assert language_change_page.verify_ukranian_language_change()