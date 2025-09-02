from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_name = (By.XPATH, "//input[@name='userName']")
        self.profile_class_No = (By.XPATH, "//input[@type='text' and @name!='userName']")
        self.profile_save_changes_button = (By.XPATH, "//button[contains(text(), 'Zapisz zmiany')]")
        self.change_name_err_message = (By.CLASS_NAME, "error-text")
        self.grade = (By.ID, "grade")
        self.error_lower_grade_message = (By.CLASS_NAME, "error-text")
        self.success_message = (By.XPATH, "//p[contains(text(), 'Dane zapisane.')]")

    def fill_profile_name(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.profile_name)).send_keys("Maciek")

    def submit_changes(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.profile_save_changes_button)).click()

    def clear_profile_name(self):
        element = self.driver.find_element(By.XPATH, "//input[@name='userName']")
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)

    def get_error_text_message(self):
        try:
            element = self.driver.wait.until(EC.visibility_of_element_located(self.change_name_err_message))
            return element.text
        except TimeoutException:
            return None

    def change_grade_lower_case(self):
        grade_low_element = self.driver.wait.until(EC.visibility_of_element_located(self.grade))
        grade_low_element.clear()
        grade_low_element.send_keys("3")

    def get_alert_message_lower_grade_case(self):
        try:
            self.driver.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert

            alert_text = alert.text
            alert.accept()

            return "Nie możesz cofnąć klasy do niższego poziomu" in alert_text

        except TimeoutException:
            return False

    def change_grade_higher_case(self):
        grade_high_element = self.driver.wait.until(EC.visibility_of_element_located(self.grade))
        grade_high_element.clear()
        grade_high_element.send_keys("9")

    def higher_grade_confirm(self):
        self.driver.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def get_alert_message_higher_grade_case(self):
        try:
            element = self.driver.wait.until(EC.visibility_of_element_located(self.error_lower_grade_message))
            return element.text
        except TimeoutException:
            return None

    def valid_grade_case(self):
        grade_low_element = self.driver.wait.until(EC.visibility_of_element_located(self.grade))
        grade_low_element.clear()
        grade_low_element.send_keys("4")

    def get_success_message(self):
        try:
            element = self.driver.wait.until(EC.presence_of_element_located(self.success_message))
            return element.text
        except TimeoutException:
            return None