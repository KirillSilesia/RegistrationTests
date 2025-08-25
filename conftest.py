import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import config

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # Set browser language to Polish
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'pl'})
    chrome_options.add_argument("--lang=pl")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
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
