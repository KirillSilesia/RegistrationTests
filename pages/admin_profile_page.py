from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AdminProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.school_applications_button = (By.XPATH,
                                           "//button[contains(@class, 'admin_tab') and text()='Wnioski rejestracyjne']")
        self.new_school_applications = (By.XPATH,
                                        "//button[contains(@class, 'filter-btn-segmented') and text()='Nowe']")
        self.approve_button = (By.XPATH, "//button[contains(text(), 'Akceptuj')]")
        self.approved_school_applications = (By.XPATH,
                                             "//button[contains(@class, 'filter-btn-segmented') and text()='Zaakceptowane']")
        self.last_school_application = None
        self.last_suggestion = None
        self.highest_id = None
        self.last_school_present = (
            By.XPATH,
            f"//div[contains(@class, 'registration-card') and contains(@class, 'pro')]"
            f"[.//span[@class='meta-label' and text()='ID:']/following-sibling::span[@class='meta-value' and normalize-space(text())='{self.highest_id}']]"
        )
        self.suggestion_text = (By.XPATH, "//*[contains(text(), 'Testing')]")
        self.description_field = (By.CLASS_NAME, "input-textarea-pro")
        self.reject_button = (By.XPATH, "//button[contains(text(), 'Odrzuć')]")
        self.rejected_applications = (By.XPATH,
                                      "//button[contains(@class, 'filter-btn-segmented') and text()='Odrzucone']")
        self.failed_message = (By.CLASS_NAME, "success-message")
        self.suggestions_button = (By.XPATH, "//button[contains(@class, 'admin-tab') and text()='Sugestie']")

    def find_last_school_application(self):
        cards = self.driver.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.registration-card.pro")
        ))

        highest_id = -1
        highest_card = None

        for card in cards:
            try:
                id_elem = card.find_element(By.CSS_SELECTOR, ".card-meta-pro .meta-value")
                id_value = int(id_elem.text.strip())
                if id_value > highest_id:
                    highest_id = id_value
                    highest_card = card
            except Exception:
                continue

        if not highest_card:
            raise Exception("No valid school application cards found.")

        try:
            self.last_school_application = highest_card.find_element(
                By.XPATH, ".//button[contains(text(), 'Szczegóły')]"
            )
        except NoSuchElementException:
            raise Exception(f"'Szczegóły' button not found in card with ID {self.highest_id}")

        self.highest_id = highest_id

    def go_to_suggestions(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_button)).click()

    def find_last_suggestion(self):
        rows = self.driver.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "tr")
        ))

        highest_id = -1
        highest_row = None

        for row in rows:
            try:
                td_elements = row.find_elements(By.TAG_NAME, "td")
                if not td_elements:
                    continue

                id_text = td_elements[0].text.strip()
                id_value = int(id_text)

                if id_value > highest_id:
                    highest_id = id_value
                    highest_row = row
            except Exception:
                continue

        if not highest_row:
            raise Exception("No valid rows with numeric IDs found.")

        try:
            self.last_suggestion = highest_row.find_element(
                By.XPATH, ".//button[contains(text(), 'Podgląd')]"
            )
        except NoSuchElementException:
            raise Exception(f"'Podgląd' button not found in row with ID {highest_id}")

        self.highest_id = highest_id

    def go_to_last_suggestion(self):
        if not self.last_suggestion:
            raise Exception("last_suggestion is not set. Call find_last_suggestion() first.")
        self.driver.wait.until(EC.element_to_be_clickable(self.last_suggestion)).click()

    def add_description_to_school_application(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.description_field)).send_keys("test")

    def reject_school_application(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.reject_button)).click()

    def go_to_rejected_school_applications(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.rejected_applications)).click()

    def is_school_rejected(self):
        self.last_school_present = (
            By.XPATH,
            f"//div[contains(@class, 'registration-card') and contains(@class, 'pro')]"
            f"[.//span[@class='meta-label' and text()='ID:']/following-sibling::span[@class='meta-value' and normalize-space(text())='{self.highest_id}']]"
        )
        try:
            self.driver.wait.until(
                EC.presence_of_element_located(self.last_school_present)
            )
            return True
        except TimeoutException:
            return False

    def is_same_suggestion(self):
        try:
            self.driver.wait.until(
                EC.presence_of_element_located(self.suggestion_text)
            )
            return True
        except TimeoutException:
            return False

    def is_failed_message(self):
        try:
            self.driver.wait.until(EC.visibility_of_element_located(self.failed_message))
            return True
        except TimeoutException:
            return False

    def go_to_last_school_application(self):
        if not self.last_school_application:
            raise Exception("last_school_application is not set. Call find_last_school_application() first.")
        self.driver.wait.until(EC.element_to_be_clickable(self.last_school_application)).click()

    def go_to_school_applications(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.school_applications_button)).click()

    def go_to_new_school_applications(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.new_school_applications)).click()

    def approve_school_application(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.approve_button)).click()

    def go_to_approved_school_applications(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.approved_school_applications)).click()

    def is_school_accepted(self):
        self.last_school_present = (
            By.XPATH,
            f"//div[contains(@class, 'registration-card') and contains(@class, 'pro')]"
            f"[.//span[@class='meta-label' and text()='ID:']/following-sibling::span[@class='meta-value' and normalize-space(text())='{self.highest_id}']]"
        )
        try:
            self.driver.wait.until(
                EC.presence_of_element_located(self.last_school_present)
            )
            return True
        except TimeoutException:
            return False

