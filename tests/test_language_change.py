from conftest import driver
from utils.assertions import assert_url_contains
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import config
import pytest
import emoji
@pytest.mark.e2e
@pytest.mark.regression

def test_language_change_to_english(driver):
    main_page = MainPage(driver)

    main_page.go_to_language()
    main_page.change_lang_to_english()
    assert main_page.verify_language_change([
        ((By.XPATH, "//button[text()='Log in']"), "Log in"),
        ((By.XPATH, "//button[text()='Register']"), "Register"),
        ((By.XPATH, "//button[text()='Submit an application for the school']"), "Submit an application for the school")
    ])

def test_language_change_to_ukranian(driver):
    main_page = MainPage(driver)

    main_page.go_to_language()
    main_page.change_lang_to_ukranian()
    assert main_page.verify_language_change([
        ((By.XPATH, "//button[text()='Увійти']"), "Увійти"),
        ((By.XPATH, "//button[text()='Зареєструватися']"), "Зареєструватися"),
        ((By.XPATH, "//button[text()='Подати заявку до школи']"), "Подати заявку до школи")
    ])