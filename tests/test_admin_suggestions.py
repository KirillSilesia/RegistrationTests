from conftest import *
from pages import main_page
from pages.logged_in_page import LoggedInPage


def test_suggestion_presence(driver_with_admin_login):
    logged_in_page = LoggedInPage(driver_with_admin_login)

    logged_in_page.go_to_suggestions()
    logged_in_page.find_last_suggestion()
    logged_in_page.go_to_last_suggestion()
    assert logged_in_page.is_same_suggestion() is True