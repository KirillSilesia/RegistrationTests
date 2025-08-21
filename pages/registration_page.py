from selenium.webdriver.common.by import By
from generators.email_generators import *
from generators.password_generators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.username_input = (By.ID, "userName")
        self.password_input = (By.ID, "password")
        self.repeat_password_input = (By.ID, "repeatPassword")
        self.grade_input = (By.ID, "grade")
        self.terms_checkbox = (By.ID, "termsAccepted")
        self.gdpr_checkbox = (By.ID, "gdprAccepted")
        self.registration_submit_button = (By.XPATH, "//*[contains(text(), 'Register')]")
        self.back_button = (By.XPATH, "//*[contains(text(), 'Back')]")

    def fill_valid_email(self):
        email_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input)
        )
        email_element.send_keys(random_email())

    def fill_special_email(self):
        self.driver.find_element(*self.email_input).sendkeys(random_email_special())

    def fill_no_domen_email(self):
        self.driver.find_element(*self.email_input).sendkeys(random_email_no_domen())

    def fill_double_at_email(self):
        self.driver.find_element(*self.email_input).sendkeys(random_email_double_at())

    def fill_without_at_email(self):
        self.driver.find_element(*self.email_input).sendkeys(random_email_without_at())

    def fill_username(self):
        self.driver.find_element(*self.username_input).send_keys("John doe")

    def fill_valid_password(self):
        self.driver.find_element(*self.password_input).send_keys("12345678")

    def fill_repeat_valid_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("12345678")

    def fill_valid_grade(self):
        self.driver.find_element(*self.grade_input).send_keys("8")

    def fill_terms_checkbox(self):
        self.driver.find_element(*self.terms_checkbox).click()

    def fill_gdpr_checkbox(self):
        self.driver.find_element(*self.gdpr_checkbox).click()

    def submit_registration(self):
        self.driver.find_element(*self.registration_submit_button).click()
