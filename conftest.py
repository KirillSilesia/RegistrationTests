import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import config
from pages.main_page import *
import time

from pages.school_registration_page import SchoolRegistrationPage
from pages.suggestions_page import SuggestionsPage


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'pl'})
    chrome_options.add_argument("--lang=pl")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(config.BASE_URL)
    driver.wait = WebDriverWait(driver, 15)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_login(driver):
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'pl'})
    chrome_options.add_argument("--lang=pl")
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Zaloguj się']]"))
    )
    login_button.click()
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "login-email")))
    email_input.send_keys(config.EMAIL)

    password_input = driver.find_element(By.ID, "login-password")
    password_input.clear()
    password_input.send_keys(config.PASSWORD)

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Zaloguj się')]")
    submit_button.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'welcome')))

    current_theme = driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
    if current_theme != "light":
        choose_theme = driver.find_element(By.CLASS_NAME, "theme-icon")
        choose_theme.click()
        light_theme = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'theme-option is-active') and contains(text(), 'Jasny')]")))
        light_theme.click()

    yield driver

@pytest.fixture(scope="function")
def driver_with_admin_login(driver):
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'pl'})
    chrome_options.add_argument("--lang=pl")
    wait = WebDriverWait(driver, 10)

    school_registration_page = SchoolRegistrationPage(driver)
    main_page = MainPage(driver)
    suggestions_page = SuggestionsPage(driver)

    main_page.go_to_school_registration()
    school_registration_page.fill_valid_school_name()
    school_registration_page.fill_valid_school_street()
    school_registration_page.fill_valid_school_building_number()
    school_registration_page.fill_valid_school_postal_code()
    school_registration_page.fill_valid_school_city()
    school_registration_page.fill_valid_school_nip()
    school_registration_page.fill_valid_school_regon()
    school_registration_page.fill_valid_school_website()
    school_registration_page.fill_valid_school_submitter_name()
    school_registration_page.fill_valid_school_submitter_role()
    school_registration_page.fill_valid_school_contact_phone()
    school_registration_page.fill_valid_school_contact_email()
    school_registration_page.accept_school_terms()
    school_registration_page.accept_school_gdpr()
    school_registration_page.click_on_voivodeship()
    school_registration_page.choose_voivodeship()
    school_registration_page.submit_school_registration()

    main_page.go_to_suggestions()
    suggestions_page.test_admin_suggestion_message()
    suggestions_page.send_suggestion()

    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Zaloguj się']]"))
    )
    time.sleep(1)
    login_button.click()
    email_input = wait.until(EC.element_to_be_clickable((By.ID, "login-email")))
    email_input.send_keys(config.EMAIL_ADMIN)

    password_input = driver.find_element(By.ID, "login-password")
    password_input.clear()
    password_input.send_keys(config.PASSWORD_ADMIN)

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Zaloguj się')]")
    submit_button.click()

    current_theme = driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
    if current_theme != "light":
        choose_theme = driver.find_element(By.CLASS_NAME, "theme-icon")
        choose_theme.click()
        light_theme = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'theme-option is-active') and contains(text(), 'Jasny')]")))
        light_theme.click()

    yield driver