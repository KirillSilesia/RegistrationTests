from pages.main_page import MainPage
from conftest import *

def test_language_change_to_english(driver):
    main_page = MainPage(driver)

    main_page.go_to_language()
    main_page.change_lang_to_english()
    assert main_page.verify_english_language_change()

def test_language_change_to_ukranian(driver):
    main_page = MainPage(driver)

    main_page.go_to_language()
    main_page.change_lang_to_ukranian()
    assert main_page.verify_ukranian_language_change()