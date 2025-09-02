from conftest import *
from pages.admin_profile_page import AdminProfilePage

def test_suggestion_presence(driver_with_admin_login):
    admin_profile_page = AdminProfilePage(driver_with_admin_login)

    admin_profile_page.go_to_suggestions()
    admin_profile_page.find_last_suggestion()
    admin_profile_page.go_to_last_suggestion()
    assert admin_profile_page.is_same_suggestion() is True