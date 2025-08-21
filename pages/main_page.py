from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_button = (By.XPATH, "//*[contains(text(), 'Register')]")

    def go_to_registration(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.registration_button)
        ).click()