from utils.global_utils import *

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.registration_button = (By.XPATH, "//*[contains(text(), 'Zarejestruj się')]")
        self.login_button = (By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
        self.language_button = (By.CLASS_NAME, "lang-label")
        self.suggestions_button = (By.XPATH, "//button[@aria-label='Dodaj sugestię']")
        self.school_registration_button = (By.XPATH, "//*[contains(text(), 'Złóż wniosek dla szkoły')]")
        self.logout_button = (By.XPATH, "//button[@title='Wyloguj']")

    def go_to_registration(self):
        self.driver.wait.until( EC.element_to_be_clickable(self.registration_button)).click()

    def go_to_school_registration(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.school_registration_button)).click()

    def go_to_suggestions(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_button)).click()

    def go_to_login(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def go_to_language(self):
        button = self.driver.wait.until(EC.presence_of_element_located(self.language_button))
        self.driver.execute_script("arguments[0].click();", button)

    def is_user_logged_in(self):
        try:
            self.driver.until(EC.visibility_of_element_located(self.logout_button))
            return True
        except:
            return False