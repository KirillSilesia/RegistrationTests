from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By



class MainPage:

    ENGLISH_LANGUAGE_ELEMENTS = [
        ((By.XPATH, "//button[text()='Log in']"), "Log in"),
        ((By.XPATH, "//button[text()='Register']"), "Register"),
        ((By.XPATH, "//button[text()='Submit an application for the school']"), "Submit an application for the school")
    ]

    UKRANIAN_LANGUAGE_ELEMENTS = [
        ((By.XPATH, "//button[text()='Увійти']"), "Увійти"),
        ((By.XPATH, "//button[text()='Зареєструватися']"), "Зареєструватися"),
        ((By.XPATH, "//button[text()='Подати заявку до школи']"), "Подати заявку до школи")
    ]

    def __init__(self, driver):
        self.driver = driver
        self.registration_button = (By.XPATH, "//*[contains(text(), 'Zarejestruj się')]")
        self.login_button = (By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
        self.language_button = (By.CLASS_NAME, "lang-switcher-caret")
        self.english_button = (By.CLASS_NAME, "lang-switcher-option")
        self.ukranian_button = (By.CSS_SELECTOR, "lang-switcher-option")
        self.suggestions_button = (By.XPATH, "//button[@aria-label='Dodaj sugestię']")
        self.suggestions_input = (By.XPATH, "//textarea[@placeholder='Co chcesz ulepszyć albo co nie działa?']")
        self.suggestions_send_button = (By.CLASS_NAME, "btn-primary")
        self.suggestions_success_message = (By.XPATH, "//*[contains(text(), 'Dziękujemy')]")
        self.suggestions_error_message = (By.XPATH, "//*[contains(text(), 'Napisz proszę')]")

    def go_to_registration(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.registration_button)
        ).click()

    def go_to_suggestions(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.suggestions_button)
        ).click()

    def valid_suggestion_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.suggestions_input)
        ).send_keys("Wow! cool app!")

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
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.suggestions_success_message)
        )
        return self.driver.find_element(*self.suggestions_success_message).text

    def get_suggestions_error_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.suggestions_error_message)
        )
        return self.driver.find_element(*self.suggestions_error_message).text

    def go_to_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def go_to_language(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.language_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def change_lang_to_english(self):
        wait = WebDriverWait(self.driver, 15)
        # Use CSS selector to get button with specified emoji text
        english_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "button.lang-switcher-option"
        )))
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.lang-switcher-option")
        target_button = None
        for btn in buttons:
            if btn.get_attribute('innerText') == '🇬🇧':
                target_button = btn
                break
        if target_button:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target_button)
            try:
                target_button.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", target_button)
        else:
            raise Exception("English language button with 🇬🇧 not found")

    def change_lang_to_ukranian(self):
        wait = WebDriverWait(self.driver, 15)
        # Use CSS selector to get button with specified emoji text
        english_button = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "button.lang-switcher-option"
        )))
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.lang-switcher-option")
        target_button = None
        for btn in buttons:
            if btn.get_attribute('innerText') == '🇺🇦':
                target_button = btn
                break
        if target_button:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target_button)
            try:
                target_button.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", target_button)
        else:
            raise Exception("Ukranian language button with 🇺🇦 not found")

    def verify_english_language_change(self, locators_with_expected_texts=None):
        if locators_with_expected_texts is None:
            locators_with_expected_texts = self.ENGLISH_LANGUAGE_ELEMENTS
        for (by, locator), expected_text in locators_with_expected_texts:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((by, locator))
                )
                actual_text = element.text.strip()
                if actual_text != expected_text:
                    print(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
                    raise AssertionError(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
            except TimeoutException:
                raise AssertionError(
                    f"Timeout error: element ({by}, {locator}) not clickable or not found in time. Expected text: '{expected_text}'"
                )
        return True

    def verify_ukranian_language_change(self, locators_with_expected_texts=None):
        if locators_with_expected_texts is None:
            locators_with_expected_texts = self.UKRANIAN_LANGUAGE_ELEMENTS
        for (by, locator), expected_text in locators_with_expected_texts:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((by, locator))
                )
                actual_text = element.text.strip()
                if actual_text != expected_text:
                    print(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
                    raise AssertionError(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
            except TimeoutException:
                raise AssertionError(
                    f"Timeout error: element ({by}, {locator}) not clickable or not found in time. Expected text: '{expected_text}'"
                )
        return True