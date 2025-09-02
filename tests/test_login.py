from conftest import *
from pages.login_page import *
from conftest import *

def test_login_valid_data(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_valid_email()
    login_page.fill_valid_password()
    login_page.submit_login()

def test_login_no_domain_email(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_no_domain_email()
    login_page.fill_valid_password()
    login_page.submit_login()
    assert login_page.get_error_message()

def test_login_double_at_email(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_double_at_email()
    login_page.fill_valid_password()
    login_page.submit_login()
    assert login_page.get_error_message()

def test_login_with_invalid_password(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_valid_email()
    login_page.fill_invalid_password()
    login_page.submit_login()
    assert login_page.login_error_message()

def test_login_with_empty_fields(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.submit_login()
    assert login_page.get_error_message()

def test_login_with_special_email(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_special_email()
    login_page.fill_valid_password()
    login_page.submit_login()
    assert login_page.login_error_message()

def test_login_with_many_login_fails(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_login()
    login_page.fill_valid_email()
    login_page.fill_invalid_password()
    for i in range(5):
        login_page.submit_login()
        assert login_page.login_error_message(), f"No error message during try nr: {i+1}"
        assert login_page.is_on_login_page(), f"User was logged in during try nr: {i+1}"

def test_login_valid_data_session_persistence(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    wait = WebDriverWait(driver, 10)

    main_page.go_to_login()
    login_page.fill_valid_email()
    login_page.fill_valid_password()
    login_page.submit_login()
    wait.until(lambda driver: login_page.is_on_login_page())

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://beta.knowlee.edu.pl")
    assert main_page.is_user_logged_in(), "The application did not recognize logged in account in the second tab"