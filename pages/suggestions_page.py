from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SuggestionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.suggestions_input = (By.XPATH, "//textarea[@placeholder='Co chcesz ulepszyć albo co nie działa?']")
        self.suggestions_send_button = (By.CLASS_NAME, "btn-primary")
        self.suggestions_success_message = (By.XPATH, "//*[contains(text(), 'Dziękujemy')]")
        self.suggestions_error_message = (By.XPATH, "//*[contains(text(), 'Napisz proszę')]")

    def valid_suggestion_message(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_input)).send_keys("Wow! cool app!")

    def invalid_suggestion_message(self, chunk="text", chunk_size=100, repetitions=501):
        field = self.driver.find_element(*self.suggestions_input)
        full_text = chunk * repetitions
        for i in range(0, len(full_text), chunk_size):
                field.send_keys(full_text[i:i + chunk_size])

    def get_real_length(self):
        field = self.driver.find_element(*self.suggestions_input)
        value = field.get_attribute("value")
        return len(value)

    def is_pasted_fully(self):
        actual_length = self.get_real_length()
        expected_length = 2004
        if actual_length != expected_length:
            return True
        else:
            raise AssertionError

    def send_suggestion(self):
        self.driver.find_element(*self.suggestions_send_button).click()

    def get_suggestions_success_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.suggestions_success_message))
        return self.driver.find_element(*self.suggestions_success_message).text

    def get_suggestions_error_message(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.suggestions_error_message))
        return self.driver.find_element(*self.suggestions_error_message).text

    def test_admin_suggestion_message(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_input)).send_keys("Testing")