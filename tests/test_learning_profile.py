from conftest import *
from pages.learning_profile_page import LearningProfilePage
from pages.logged_in_page import *

def test_access_learning_profile(driver_with_login):
    learning_profile_page = LearningProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    learning_profile_page.close_learning_profile()
    assert learning_profile_page.is_succeed() is not True

def test_access_change_learning_profile(driver_with_login):
    learning_profile_page = LearningProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    learning_profile_page.change_learning_profile()
    learning_profile_page.change_learning_profile_abort()
    assert learning_profile_page.is_succeed() is not True

def test_learning_profile_valid_data(driver_with_login):
    learning_profile_page = LearningProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    learning_profile_page.change_learning_profile()
    learning_profile_page.choose_learning_profile_first_dropdown()
    learning_profile_page.change_learning_profile_first_answer()
    learning_profile_page.choose_learning_profile_second_dropdown()
    learning_profile_page.change_learning_profile_second_answer()
    learning_profile_page.choose_learning_profile_third_dropdown()
    learning_profile_page.change_learning_profile_third_answer()
    learning_profile_page.choose_learning_profile_fourth_dropdown()
    learning_profile_page.change_learning_profile_fourth_answer()
    learning_profile_page.choose_learning_profile_fifth_dropdown()
    learning_profile_page.change_learning_profile_fifth_answer()
    learning_profile_page.choose_learning_profile_sixth_dropdown()
    learning_profile_page.change_learning_profile_sixth_answer()
    learning_profile_page.choose_learning_profile_seventh_field()
    learning_profile_page.change_learning_profile_seventh_valid_answer()
    learning_profile_page.submit_learning_profile()
    assert learning_profile_page.is_succeed() is True

def test_learning_profile_invalid_data(driver_with_login):
    learning_profile_page = LearningProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    learning_profile_page.change_learning_profile()
    learning_profile_page.choose_learning_profile_first_dropdown()
    learning_profile_page.change_learning_profile_first_answer()
    learning_profile_page.choose_learning_profile_second_dropdown()
    learning_profile_page.change_learning_profile_second_answer()
    learning_profile_page.choose_learning_profile_third_dropdown()
    learning_profile_page.change_learning_profile_third_answer()
    learning_profile_page.choose_learning_profile_fourth_dropdown()
    learning_profile_page.change_learning_profile_fourth_answer()
    learning_profile_page.choose_learning_profile_fifth_dropdown()
    learning_profile_page.change_learning_profile_fifth_answer()
    learning_profile_page.choose_learning_profile_sixth_dropdown()
    learning_profile_page.change_learning_profile_sixth_answer()
    learning_profile_page.choose_learning_profile_seventh_field()
    learning_profile_page.change_learning_profile_seventh_invalid_answer()
    learning_profile_page.submit_learning_profile()
    assert learning_profile_page.is_error() is True

def test_learning_profile_empty_fields(driver_with_login):
    learning_profile_page = LearningProfilePage(driver_with_login)
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    learning_profile_page.change_learning_profile()
    learning_profile_page.submit_learning_profile()

    assert learning_profile_page.is_learning_profile_modal_open() is True