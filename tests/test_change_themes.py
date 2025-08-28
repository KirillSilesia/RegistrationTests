from pages.logged_in_page import LoggedInPage
from conftest import *


def test_change_theme_to_dark(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.click_on_theme()
    logged_in_page.choose_dark_theme()
    assert logged_in_page.if_changed_to_dark_theme() is True

def test_change_theme_to_high_contrast(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.click_on_theme()
    logged_in_page.choose_high_contrast_theme()
    assert logged_in_page.if_changed_to_high_contrast_theme() is True

def test_change_theme_to_light(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.click_on_theme()
    logged_in_page.choose_high_contrast_theme()
    logged_in_page.click_on_theme()
    logged_in_page.choose_light_theme()
    assert logged_in_page.if_changed_to_light_theme() is True