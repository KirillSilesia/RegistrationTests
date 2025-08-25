from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.registration_button = (By.XPATH, "//*[contains(text(), 'Zarejestruj się')]")
        self.login_button = (By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
        self.language_button = (By.CLASS_NAME, "lang-switcher-caret")
        self.english_button = (By.CLASS_NAME, "lang-switcher-option")
        self.ukranian_button = (By.CSS_SELECTOR, "lang-switcher-option")

    def go_to_registration(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.registration_button)
        ).click()

    def go_to_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def go_to_language(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.language_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    # def change_lang_to_english(self):
    #     wait = WebDriverWait(self.driver, 5)
    #     # Wait until language buttons are present
    #     lang_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lang-switcher-option")))
    #     # Click button that contains the 🇬🇧 emoji text
    #     for button in lang_buttons:
    #         if '🇬🇧' in button.text:
    #             button.click()
    #             break

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

    # def verify_language_change(self, locators_with_expected_texts):
    #     for locator, expected_text in locators_with_expected_texts:
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located(locator)
    #         )
    #         actual_text = element.text
    #         assert actual_text == expected_text, f"Expected '{expected_text}' got '{actual_text}'"
    def verify_language_change(self, locators_with_expected_texts):
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