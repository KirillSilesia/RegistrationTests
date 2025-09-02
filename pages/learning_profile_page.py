from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LearningProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.learning_profile_change_button = (By.XPATH, "//button[contains(text(), 'Zmień profil')]")
        self.learning_profile_close_button = (By.XPATH, "//button[contains(text(), 'Zamknij')]")
        self.learning_profile_first_dropdown = (By.ID, "q-LEARNING_STYLE")
        self.learning_profile_second_dropdown = (By.ID, "q-MOTIVATION_TYPE")
        self.learning_profile_third_dropdown = (By.ID, "q-FOCUS_LEVEL")
        self.learning_profile_fourth_dropdown = (By.ID, "q-PATIENCE_LEVEL")
        self.learning_profile_fifth_dropdown = (By.ID, "q-SELF_CONFIDENCE")
        self.learning_profile_sixth_dropdown = (By.ID, "q-ORGANIZATION_STYLE")
        self.learning_profile_seventh_field = (By.ID, "q-SPECIAL_NEEDS")
        self.learning_profile_submit_change_button = (By.XPATH, "//button[contains(text(), 'Zapisz profil')]")
        self.learning_profile_abort_change_button = (By.XPATH, "//button[contains(text(), 'Zamknij')]")
        self.learning_profile_first_answer = (By.XPATH, "//*[contains(text(), 'Czytając')]")
        self.learning_profile_second_answer = (By.XPATH, "//*[contains(text(), 'Pochwały')]")
        self.learning_profile_third_answer = (By.XPATH, "//*[contains(text(), 'Tak')]")
        self.learning_profile_fourth_answer = (By.XPATH, "//*[contains(text(), 'Próbuję dalej')]")
        self.learning_profile_fifth_answer = (By.XPATH, "//*[contains(text(), 'Pewnie')]")
        self.learning_profile_sixth_answer = (By.XPATH, "//*[contains(text(), 'Lubię mieć plan')]")
        self.learning_profile_error = (By.CLASS_NAME, "error")
        self.is_succeed_message = (By.XPATH, "//*[contains(text(), 'Podsumowanie profilu:')]")

    def close_learning_profile(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_close_button)).click()

    def change_learning_profile(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_change_button)).click()

    def change_learning_profile_abort(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_abort_change_button)).click()

    def choose_learning_profile_first_dropdown(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_first_dropdown)).click()

    def change_learning_profile_first_answer(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_first_answer)).click()

    def choose_learning_profile_second_dropdown(self):
        self.driver.find_element(*self.learning_profile_second_dropdown).click()

    def change_learning_profile_second_answer(self):
        self.driver.find_element(*self.learning_profile_second_answer).click()

    def choose_learning_profile_third_dropdown(self):
        self.driver.find_element(*self.learning_profile_third_dropdown).click()

    def change_learning_profile_third_answer(self):
        self.driver.find_element(*self.learning_profile_third_answer).click()

    def choose_learning_profile_fourth_dropdown(self):
        self.driver.find_element(*self.learning_profile_fourth_dropdown).click()

    def change_learning_profile_fourth_answer(self):
        self.driver.find_element(*self.learning_profile_fourth_answer).click()

    def choose_learning_profile_fifth_dropdown(self):
        self.driver.find_element(*self.learning_profile_fifth_dropdown).click()

    def change_learning_profile_fifth_answer(self):
        self.driver.find_element(*self.learning_profile_fifth_answer).click()

    def choose_learning_profile_sixth_dropdown(self):
        self.driver.find_element(*self.learning_profile_sixth_dropdown).click()

    def change_learning_profile_sixth_answer(self):
        self.driver.find_element(*self.learning_profile_sixth_answer).click()

    def choose_learning_profile_seventh_field(self):
        self.driver.find_element(*self.learning_profile_seventh_field).click()

    def change_learning_profile_seventh_valid_answer(self):
        self.driver.find_element(*self.learning_profile_seventh_field).send_keys("Lubię jeść coś gdy się uczę")

    def change_learning_profile_seventh_invalid_answer(self):
        self.driver.find_element(*self.learning_profile_seventh_field).send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def submit_learning_profile(self):
        self.driver.find_element(*self.learning_profile_submit_change_button).click()

    def is_error(self):
        try:
            self.driver.wait.until(EC.visibility_of_element_located(self.learning_profile_error))
            return True
        except TimeoutException:
            return False

    def is_succeed(self):
        try:
            self.driver.wait.until(EC.visibility_of_element_located(self.is_succeed_message))
            return True
        except TimeoutException:
            return False

    def is_learning_profile_modal_open(self):
        try:
            modal = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
            return modal.is_displayed()
        except NoSuchElementException:
            return False