from conftest import *
from pages.logged_in_page import *

def test_access_learning_profile(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    logged_in_page.close_learning_profile()
    assert logged_in_page.is_succeed() is not True

def test_access_change_learning_profile(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    logged_in_page.change_learning_profile()
    logged_in_page.change_learning_profile_abort()
    assert logged_in_page.is_succeed() is not True

def test_learning_profile_valid_data(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    logged_in_page.change_learning_profile()
    logged_in_page.choose_learning_profile_first_dropdown()
    logged_in_page.change_learning_profile_first_answer()
    logged_in_page.choose_learning_profile_second_dropdown()
    logged_in_page.change_learning_profile_second_answer()
    logged_in_page.choose_learning_profile_third_dropdown()
    logged_in_page.change_learning_profile_third_answer()
    logged_in_page.choose_learning_profile_fourth_dropdown()
    logged_in_page.change_learning_profile_fourth_answer()
    logged_in_page.choose_learning_profile_fifth_dropdown()
    logged_in_page.change_learning_profile_fifth_answer()
    logged_in_page.choose_learning_profile_sixth_dropdown()
    logged_in_page.change_learning_profile_sixth_answer()
    logged_in_page.choose_learning_profile_seventh_field()
    logged_in_page.change_learning_profile_seventh_valid_answer()
    logged_in_page.submit_learning_profile()
    assert logged_in_page.is_succeed() is True

def test_learning_profile_invalid_data(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    logged_in_page.change_learning_profile()
    logged_in_page.choose_learning_profile_first_dropdown()
    logged_in_page.change_learning_profile_first_answer()
    logged_in_page.choose_learning_profile_second_dropdown()
    logged_in_page.change_learning_profile_second_answer()
    logged_in_page.choose_learning_profile_third_dropdown()
    logged_in_page.change_learning_profile_third_answer()
    logged_in_page.choose_learning_profile_fourth_dropdown()
    logged_in_page.change_learning_profile_fourth_answer()
    logged_in_page.choose_learning_profile_fifth_dropdown()
    logged_in_page.change_learning_profile_fifth_answer()
    logged_in_page.choose_learning_profile_sixth_dropdown()
    logged_in_page.change_learning_profile_sixth_answer()
    logged_in_page.choose_learning_profile_seventh_field()
    logged_in_page.change_learning_profile_seventh_invalid_answer()
    logged_in_page.submit_learning_profile()
    assert logged_in_page.is_error() is True

# def test_learning_profile_empty_fields(driver_with_login):
#     logged_in_page = LoggedInPage(driver_with_login)
#
#     logged_in_page.go_to_learning_profile()
#     logged_in_page.change_learning_profile()
#     logged_in_page.submit_learning_profile()
#     time.sleep(5)
#     assert (logged_in_page.is_pop_up_error()) is True

def test_learning_profile_empty_fields(driver_with_login):
    logged_in_page = LoggedInPage(driver_with_login)

    logged_in_page.go_to_learning_profile()
    logged_in_page.change_learning_profile()
    logged_in_page.submit_learning_profile()

    assert logged_in_page.is_learning_profile_modal_open() is True