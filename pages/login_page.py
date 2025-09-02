from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from generators.email_generators import *

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "login-email")
        self.password_input = (By.ID, "login-password")
        self.login_submit_button = (By.XPATH, "//*[contains(text(), 'Zaloguj')]")
        self.error_message = (By.CLASS_NAME, "login-error-text")
        self.login_error = (By.CLASS_NAME, "login-error-message")

    def fill_valid_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys("maciejkotuczen1@gmail.com")

    def fill_no_domain_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_no_domain())

    def fill_without_at_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_without_at())

    def fill_special_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_special())

    def fill_double_at_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_double_at())

    def fill_nonexisting_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys("marekfajny@gmail.com")

    def fill_valid_password(self):
        self.driver.find_element(*self.password_input).send_keys("haselko123456@1!")

    def fill_invalid_password(self):
        self.driver.find_element(*self.password_input).send_keys("haselko123456@1")

    def submit_login(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.login_submit_button)).click()

    def get_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.error_message))
        return self.driver.find_element(*self.error_message).text

    def login_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.login_error))
        return self.driver.find_element(*self.login_error).text

    def is_on_login_page(self):
        return self.driver.current_url.endswith("/login")