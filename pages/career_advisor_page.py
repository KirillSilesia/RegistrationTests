from selenium.common import TimeoutException
from utils.global_utils import *

class CareerAdvisorPage:
    def __init__(self, driver):
        self.driver = driver
        self.abort_button = (By.XPATH, "//button[contains(normalize-space(.), 'Wróć')]")
        self.change_career_advisor_button = (By.XPATH, "//button[contains(normalize-space(.), 'Chcę zmienić odpowiedzi')]")
        self.submit_career_advisor_button = (By.XPATH, "//button[contains(normalize-space(.), 'Wyślij odpowiedzi')]")
        self.success_message = (By.XPATH, "//*[contains(text(), 'Wynik doradcy zawodowego')]")
        self.career_advisor_first_field = (By.ID, "FREE_TIME_ACTIVITY")
        self.career_advisor_second_field = (By.ID, "FUTURE_IDEA")
        self.career_advisor_third_radio = (By.NAME, "CREATIVE_ACTIVITIES")
        self.career_advisor_fourth_radio = (By.NAME, "TECHNICAL_TASKS")
        self.career_advisor_fifth_radio = (By.NAME, "ANALYTICAL_THINKING")
        self.career_advisor_sixth_radio = (By.NAME, "HELPING_PEOPLE")
        self.career_advisor_seventh_radio = (By.NAME, "TAKING_INITIATIVE")
        self.career_advisor_eighth_radio = (By.NAME, "STRUCTURED_WORK")
        self.career_advisor_ninth_radio = (By.NAME, "PUBLIC_SPEAKING_COMFORT")
        self.career_advisor_tenth_radio = (By.NAME, "WORKING_STYLE")
        self.career_advisor_eleventh_radio = (By.NAME, "FOCUS_DURATION")
        self.career_advisor_twelfth_radio = (By.NAME, "INDOOR_OR_OUTDOOR")
        self.career_advisor_thirteenth_radio = (By.NAME, "ORGANIZATION_SKILLS")
        self.career_advisor_fourteenth_radio = (By.NAME, "GROUP_STRESS")
        self.career_advisor_fifteenth_field = (By.ID, "BOREDOM_CAUSES")
        self.career_advisor_sixteenth_radio = (By.NAME, "STRESS_REACTIONS")
        self.career_advisor_seventeenth_field = (By.ID, "FAVORITE_SUBJECT")
        self.career_advisor_eighteenth_radio = (By.NAME, "SCHOOL_PREFERENCE")
        self.failed_message = (By.XPATH, "//*[contains(text(), 'Nie udało się wysłać odpowiedzi')]")

    def abort_career_advisor(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.abort_button)).click()

    def change_career_advisor(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.change_career_advisor_button)).click()

    def submit_career_advisor_changes(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.submit_career_advisor_button)).click()

    def is_succeed(self):
        try:
            self.driver.wait.until(EC.visibility_of_element_located(self.success_message))
            return True
        except TimeoutException:
            return False

    def is_failed(self):
        try:
            self.driver.wait.until(EC.visibility_of_element_located(self.failed_message))
            return True
        except TimeoutException:
            return False

    def select_first_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_first_field)).click()

    def valid_first_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_first_field)).send_keys("piję herbatę")

    def invalid_first_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_first_field)).send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def select_second_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_second_field)).click()

    def valid_second_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_second_field)).send_keys("prezydentem")

    def invalid_second_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_second_field)).send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def select_third_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_third_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_fourth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_fourth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_fifth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_fifth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_sixth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_sixth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_seventh_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_seventh_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_eighth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_eighth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_ninth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_ninth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_tenth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_tenth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_eleventh_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_eleventh_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_twelfth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_twelfth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_thirteenth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_thirteenth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_fourteenth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_fourteenth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_fifteenth_field(self):
        self.driver.wait.until(EC.presence_of_element_located(self.career_advisor_fifteenth_field)).click()

    def valid_fifteenth_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_fifteenth_field)).send_keys("chemia")

    def invalid_fifteenth_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_fifteenth_field)).send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def select_sixteenth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_sixteenth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()

    def select_seventeenth_field(self):
        self.driver.wait.until(EC.presence_of_element_located(self.career_advisor_seventeenth_field)).click()

    def valid_seventeenth_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_seventeenth_field)).send_keys("matematyka")

    def invalid_seventeenth_field(self):
        self.driver.wait.until(EC.visibility_of_element_located(self.career_advisor_seventeenth_field)).send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")

    def select_eighteenth_radio(self):
        radio_buttons = self.driver.wait.until(EC.presence_of_all_elements_located(self.career_advisor_eighteenth_radio))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radio_buttons[0])
        radio_buttons[0].click()