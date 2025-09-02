from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LanguageChangePage:

    ENGLISH_LANGUAGE_ELEMENTS = [
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(1)"), "Log in"),
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(2)"), "Register"),
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(3)"), "Submit an application for school")
    ]

    UKRANIAN_LANGUAGE_ELEMENTS = [
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(1)"), "Увійти"),
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(2)"), "Зареєструватися"),
        ((By.CSS_SELECTOR, "button.btn.btn--small:nth-of-type(3)"), "Подати заявку до школи")
    ]

    def __init__(self, driver):
        self.driver = driver
        self.english_button = (By.XPATH, "//*[contains(@class, 'lang-text') and contains(text(), 'English')]")
        self.ukrainian_button = (By.XPATH, "//*[contains(@class, 'lang-text') and contains(text(), 'Українська')]")
        self.language_button = (By.CLASS_NAME, "lang-label")

    def change_lang_to_english(self):
        self.driver.wait.until(EC.element_to_be_clickable((self.english_button))).click()

    def change_lang_to_ukranian(self):
        self.driver.wait.until(EC.element_to_be_clickable((self.ukrainian_button))).click()

    def verify_english_language_change(self, locators_with_expected_texts=None):
        self.driver.wait.until(EC.element_to_be_clickable((self.language_button)))
        if locators_with_expected_texts is None:
            locators_with_expected_texts = self.ENGLISH_LANGUAGE_ELEMENTS
        for (by, locator), expected_text in locators_with_expected_texts:
            try:
                element = self.driver.wait.until(EC.element_to_be_clickable((by, locator)))
                actual_text = element.text.strip()
            except StaleElementReferenceException:
                element = self.driver.wait.until(EC.element_to_be_clickable((by, locator)))
                actual_text = element.text.strip()
            if actual_text != expected_text:
                    print(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
                    raise AssertionError(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")

    def verify_ukranian_language_change(self, locators_with_expected_texts=None):
        self.driver.wait.until(EC.element_to_be_clickable((self.language_button)))
        if locators_with_expected_texts is None:
            locators_with_expected_texts = self.UKRANIAN_LANGUAGE_ELEMENTS
        for (by, locator), expected_text in locators_with_expected_texts:
            try:
                element = self.driver.wait.until(EC.element_to_be_clickable((by, locator)))
                actual_text = element.text.strip()
            except StaleElementReferenceException:
                element = self.driver.wait.until(EC.element_to_be_clickable((by, locator)))
                actual_text = element.text.strip()
            if actual_text != expected_text:
                print(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
                raise AssertionError(f"Text mismatch: expected '{expected_text}', got '{actual_text}'")
