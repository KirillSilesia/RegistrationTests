import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import config


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

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_login(driver):
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zaloguj się')]"))
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

    yield driver
