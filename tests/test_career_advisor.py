from conftest import *
from pages.logged_in_page import *
from pages.career_advisor_page import *

def test_access_career_advisor(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    career_advisor_page = CareerAdvisorPage(driver_with_login)

    logged_in_page.go_to_career_advisor()
    career_advisor_page.abort_career_advisor()
    assert driver_with_login.current_url == "https://beta.knowlee.edu.pl/"

def test_change_career_advisor_abort(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    career_advisor_page = CareerAdvisorPage(driver_with_login)

    logged_in_page.go_to_career_advisor()
    career_advisor_page.change_career_advisor()
    career_advisor_page.abort_career_advisor()
    assert driver_with_login.current_url == "https://beta.knowlee.edu.pl/"

def test_change_career_advisor_empty_fields(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    career_advisor_page = CareerAdvisorPage(driver_with_login)

    logged_in_page.go_to_career_advisor()
    career_advisor_page.change_career_advisor()
    career_advisor_page.submit_career_advisor_changes()
    assert career_advisor_page.is_input_invalid("#FREE_TIME_ACTIVITY") is True

def test_change_career_advisor_valid_data(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)
    career_advisor_page = CareerAdvisorPage(driver_with_login)

    logged_in_page.go_to_career_advisor()
    career_advisor_page.change_career_advisor()
    career_advisor_page.select_first_field()
    career_advisor_page.valid_first_field()
    career_advisor_page.select_second_field()
    career_advisor_page.valid_second_field()
    career_advisor_page.select_third_radio()
    career_advisor_page.select_fourth_radio()
    career_advisor_page.select_fifth_radio()
    career_advisor_page.select_sixth_radio()
    career_advisor_page.select_seventh_radio()
    career_advisor_page.select_eighth_radio()
    career_advisor_page.select_ninth_radio()
    career_advisor_page.select_tenth_radio()
    career_advisor_page.select_eleventh_radio()
    career_advisor_page.select_twelfth_radio()
    career_advisor_page.select_thirteenth_radio()
    career_advisor_page.select_fourteenth_radio()
    career_advisor_page.select_fifteenth_radio()
    career_advisor_page.select_sixteenth_radio()
    career_advisor_page.select_seventeenth_field()
    career_advisor_page.valid_seventeenth_field()
    career_advisor_page.select_eighteenth_radio()
    career_advisor_page.select_nineteenth_field()
    career_advisor_page.valid_nineteenth_field()
    career_advisor_page.select_twenty_radio()
    career_advisor_page.select_twentyone_radio()
    career_advisor_page.submit_career_advisor_changes()
    assert career_advisor_page.is_succeed() is True