from pages.logged_in_page import LoggedInPage
from pages.profile_page import ProfilePage
from conftest import *

def test_change_lower_edge_case_grade(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    profile_page = ProfilePage(driver_with_login)

    logged_in_page.go_to_profile()
    profile_page.change_grade_lower_case()
    profile_page.submit_changes()
    assert profile_page.get_alert_message_lower_grade_case()

def test_change_higher_edge_case_grade(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    profile_page = ProfilePage(driver_with_login)

    logged_in_page.go_to_profile()
    profile_page.change_grade_higher_case()
    profile_page.submit_changes()
    profile_page.higher_grade_confirm()

    error_text = profile_page.get_alert_message_higher_grade_case()
    assert error_text == "Klasa powinna być w przedziale od 4 do 8"

def test_change_grade_valid(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    profile_page = ProfilePage(driver_with_login)

    logged_in_page.go_to_profile()
    profile_page.valid_grade_case()
    profile_page.submit_changes()

    success_text = profile_page.get_success_message()
    assert success_text == "Dane zapisane."