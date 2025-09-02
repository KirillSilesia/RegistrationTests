from utils.global_utils import *

class LoggedInPage:
    def __init__(self, driver):
        self.driver = driver
        self.learning_profile_button = (By.XPATH, "//button[contains(normalize-space(.), 'Jak lubię się uczyć')]")
        self.learning_profile_career_advisor_button = (By.XPATH, "//button[contains(normalize-space(.), 'Doradca zawodowy')]")
        self.theme_changer = (By.CLASS_NAME, "theme-icon")
        self.dark_theme = (By.XPATH, "//button[contains(@class, 'theme-option') and .//span[normalize-space()='Ciemny']]")
        self.high_contrast_theme = (By.XPATH, "//button[contains(@class, 'theme-option') and .//span[normalize-space()='Wysoki kontrast']]")
        self.light_theme = (By.XPATH, "//button[contains(@class, 'theme-option') and .//span[normalize-space()='Jasny']]")
        self.profile_button = (By.XPATH, "//img[@alt='Awatar']")

    def go_to_learning_profile(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_button)).click()

    def click_on_theme(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.theme_changer)).click()

    def go_to_profile(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.profile_button)).click()

    def choose_dark_theme(self):
        button = self.driver.wait.until(EC.element_to_be_clickable(self.dark_theme))
        self.driver.execute_script("arguments[0].click();", button)

    def choose_high_contrast_theme(self):
        button = self.driver.wait.until(EC.element_to_be_clickable(self.high_contrast_theme))
        self.driver.execute_script("arguments[0].click();", button)

    def choose_light_theme(self):
        button = self.driver.wait.until(EC.element_to_be_clickable(self.light_theme))
        self.driver.execute_script("arguments[0].click();", button)

    def if_changed_to_light_theme(self):
        try:
            current_theme = self.driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
            return current_theme == "light"
        except Exception as e:
            print(f"Error checking theme: {e}")
            return False

    def if_changed_to_dark_theme(self):
        try:
            current_theme = self.driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
            return current_theme == "dark"
        except Exception as e:
            print(f"Error checking theme: {e}")
            return False

    def if_changed_to_high_contrast_theme(self):
        try:
            current_theme = self.driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
            return current_theme == "hc"
        except Exception as e:
            print(f"Error checking theme: {e}")
            return False

    def go_to_career_advisor(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.learning_profile_career_advisor_button)).click()