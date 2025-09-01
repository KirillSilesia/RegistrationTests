from conftest import *
from pages.logged_in_page import *

def test_admin_accept_school_application(driver_with_admin_login):
    logged_in_page = LoggedInPage(driver_with_admin_login)

    logged_in_page.go_to_new_school_applications()
    logged_in_page.find_last_school_application()
    logged_in_page.go_to_last_school_application()
    logged_in_page.approve_school_application()
    logged_in_page.go_to_approved_school_applications()

    assert logged_in_page.is_school_accepted() is True

def test_admin_reject_school_application(driver_with_admin_login):
    logged_in_page = LoggedInPage(driver_with_admin_login)

    logged_in_page.go_to_new_school_applications()
    logged_in_page.find_last_school_application()
    logged_in_page.go_to_last_school_application()
    logged_in_page.add_description_to_school_application()
    logged_in_page.reject_school_application()
    logged_in_page.go_to_rejected_school_applications()

    assert logged_in_page.is_school_rejected() is True

def test_admin_reject_school_application_without_description(driver_with_admin_login):
    logged_in_page = LoggedInPage(driver_with_admin_login)

    logged_in_page.go_to_new_school_applications()
    logged_in_page.find_last_school_application()
    logged_in_page.go_to_last_school_application()
    logged_in_page.reject_school_application()

    assert logged_in_page.is_failed_message() is True