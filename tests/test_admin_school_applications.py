from conftest import *
from pages.admin_profile_page import AdminProfilePage

def test_admin_accept_school_application(driver_with_admin_login):
    admin_profile_page = (AdminProfilePage(driver_with_admin_login))

    admin_profile_page.go_to_new_school_applications()
    admin_profile_page.find_last_school_application()
    admin_profile_page.go_to_last_school_application()
    admin_profile_page.approve_school_application()
    admin_profile_page.go_to_approved_school_applications()

    assert admin_profile_page.is_school_accepted() is True

def test_admin_reject_school_application(driver_with_admin_login):
    admin_profile_page = AdminProfilePage(driver_with_admin_login)

    admin_profile_page.go_to_new_school_applications()
    admin_profile_page.find_last_school_application()
    admin_profile_page.go_to_last_school_application()
    admin_profile_page.add_description_to_school_application()
    admin_profile_page.reject_school_application()
    admin_profile_page.go_to_rejected_school_applications()

    assert admin_profile_page.is_school_rejected() is True

def test_admin_reject_school_application_without_description(driver_with_admin_login):
    admin_profile_page = AdminProfilePage(driver_with_admin_login)

    admin_profile_page.go_to_new_school_applications()
    admin_profile_page.find_last_school_application()
    admin_profile_page.go_to_last_school_application()
    admin_profile_page.reject_school_application()

    assert admin_profile_page.is_failed_message() is True