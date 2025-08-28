from generators.email_generators import *
from utils.global_utils import *

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
        self.registration_submit_button = (By.XPATH, "//*[contains(text(), 'Zarejestruj się')]")
        self.back_button = (By.XPATH, "//*[contains(text(), 'Powrót')]")
        self.success_message = (By.XPATH, "//*[contains(text(), 'Sprawdź swoją skrzynkę')]")
        self.error_message = (By.CLASS_NAME, "register-error-text")
        self.register_error = (By.CLASS_NAME, "register-error-message")
        self.checkbox_error_message = (By.CLASS_NAME, "school-reg-error")

    def fill_valid_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email())

    def fill_special_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_special())

    def fill_no_domain_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_no_domain())

    def fill_double_at_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_double_at())

    def fill_without_at_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(random_email_without_at())

    def fill_existing_email(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys("johnsenior12345678@gmail.com")

    def fill_username(self):
        self.driver.find_element(*self.username_input).send_keys("John doe")

    def fill_valid_password(self):
        self.driver.find_element(*self.password_input).send_keys("12345678")

    def fill_too_short_password(self):
        self.driver.find_element(*self.password_input).send_keys("1234")

    def fill_repeat_too_short_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("1234")

    def fill_repeat_valid_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("12345678")

    def fill_repeat_not_same_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("123456789")

    def fill_too_long_password(self):
        self.driver.find_element(*self.password_input).send_keys("12345678910111213141516171819202122232425262728293031323334353637383940123456789012345678901234567890")

    def fill_repeat_too_long_password(self):
        self.driver.find_element(*self.repeat_password_input).send_keys("12345678910111213141516171819202122232425262728293031323334353637383940123456789012345678901234567890")

    def fill_valid_grade(self):
        self.driver.find_element(*self.grade_input).send_keys("8")

    def fill_invalid_grade(self):
        self.driver.find_element(*self.grade_input).send_keys("9")

    def fill_terms_checkbox(self):
        self.driver.find_element(*self.terms_checkbox).click()

    def fill_gdpr_checkbox(self):
        self.driver.find_element(*self.gdpr_checkbox).click()

    def submit_registration(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.registration_submit_button)).click()

    def get_success_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.success_message))
        return self.driver.find_element(*self.success_message).text

    def get_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.error_message))
        return self.driver.find_element(*self.error_message).text

    def checkbox_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.checkbox_error_message))
        return self.driver.find_element(*self.checkbox_error_message).text

    def register_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.register_error))
        return self.driver.find_element(*self.register_error).text