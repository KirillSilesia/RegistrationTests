from conftest import *
from pages.logged_in_page import LoggedInPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

def test_change_username(driver_with_login):
    profile_page = ProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_profile()
    profile_page.clear_profile_name()
    profile_page.fill_profile_name()
    profile_page.submit_changes()
    assert profile_page.get_error_text_message() is None

def test_change_empty_username(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    profile_page = ProfilePage(driver_with_login)

    logged_in_page.go_to_profile()
    profile_page.clear_profile_name()
    profile_page.submit_changes()
    assert profile_page.get_error_text_message()