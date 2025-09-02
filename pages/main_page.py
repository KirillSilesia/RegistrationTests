from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from generators.email_generators import *
from generators.nip_generators import *
from utils.global_utils import *
from selenium.common.exceptions import StaleElementReferenceException

class MainPage:

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
        self.registration_button = (By.XPATH, "//*[contains(text(), 'Zarejestruj się')]")
        self.login_button = (By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
        self.language_button = (By.CLASS_NAME, "lang-label")
        self.english_button = (By.XPATH, "//*[contains(@class, 'lang-text') and contains(text(), 'English')]")
        self.ukrainian_button = (By.XPATH, "//*[contains(@class, 'lang-text') and contains(text(), 'Українська')]")
        self.suggestions_button = (By.XPATH, "//button[@aria-label='Dodaj sugestię']")
        self.suggestions_input = (By.XPATH, "//textarea[@placeholder='Co chcesz ulepszyć albo co nie działa?']")
        self.suggestions_send_button = (By.CLASS_NAME, "btn-primary")
        self.suggestions_success_message = (By.XPATH, "//*[contains(text(), 'Dziękujemy')]")
        self.suggestions_error_message = (By.XPATH, "//*[contains(text(), 'Napisz proszę')]")
        self.school_registration_button = (By.XPATH, "//*[contains(text(), 'Złóż wniosek dla szkoły')]")
        self.submit_school_registration_button = (By.XPATH, "//*[contains(text(), 'Wyślij wniosek')]")
        self.school_name_field = (By.ID, "schoolName")
        self.school_street_field = (By.ID, "street")
        self.school_building_number = (By.ID, "buildingNumber")
        self.school_postal_code = (By.ID, "postalCode")
        self.school_city = (By.ID, "city")
        self.school_nip = (By.ID, "nip")
        self.school_regon = (By.ID, "regon")
        self.school_website = (By.ID, "website")
        self.school_submitter_name = (By.ID, "submitterName")
        self.school_submitter_role = (By.ID, "submitterRole")
        self.school_contact_phone = (By.ID, "contactPhone")
        self.school_contact_email = (By.ID, "contactEmail")
        self.school_voivodeship = (By.ID, "voivodeship")
        self.school_terms_accepted = (By.ID, "termsAccepted")
        self.school_gdpr_accepted = (By.ID, "gdprAccepted")
        self.silesian_voivodeship = (By.XPATH, "//*[contains(text(), 'śląskie')]")
        self.school_error_message = (By.CLASS_NAME, "school-reg-error")
        self.logout_button = (By.CLASS_NAME, "btn btn--danger logout-btn hdr-btn")

    def go_to_registration(self):
        self.driver.wait.until( EC.element_to_be_clickable(self.registration_button)).click()

    def log_out(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.logout_button)).click()

    def go_to_school_registration(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.school_registration_button)).click()

    def fill_valid_school_name(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.school_name_field)).send_keys("test school name")

    def fill_valid_school_street(self):
        self.driver.find_element(*self.school_street_field).send_keys("test street name")

    def fill_valid_school_building_number(self):
        self.driver.find_element(*self.school_building_number).send_keys("test building number")

    def fill_valid_school_postal_code(self):
        self.driver.find_element(*self.school_postal_code).send_keys("00000")

    def fill_invalid_school_postal_code(self):
        self.driver.find_element(*self.school_postal_code).send_keys("0000000")

    def fill_valid_school_city(self):
        self.driver.find_element(*self.school_city).send_keys("test city")

    def fill_valid_school_nip(self):
        self.driver.find_element(*self.school_nip).send_keys(generate_nip())

    def fill_invalid_school_nip(self):
        self.driver.find_element(*self.school_nip).send_keys("1234567890")

    def fill_invalid_letters_school_nip(self):
        self.driver.find_element(*self.school_nip).send_keys("test nip")

    def fill_valid_school_regon(self):
        self.driver.find_element(*self.school_regon).send_keys("013928775")

    def fill_invalid_school_regon(self):
        self.driver.find_element(*self.school_regon).send_keys("123456789")

    def fill_invalid_letters_school_regon(self):
        self.driver.find_element(*self.school_regon).send_keys("test regon")

    def fill_valid_school_website(self):
        self.driver.find_element(*self.school_website).send_keys("www.testwebsite.pl")

    def fill_valid_school_submitter_name(self):
        self.driver.find_element(*self.school_submitter_name).send_keys("test submitter name")

    def fill_valid_school_submitter_role(self):
        self.driver.find_element(*self.school_submitter_role).send_keys("test submitter role")

    def fill_valid_school_contact_phone(self):
        self.driver.find_element(*self.school_contact_phone).send_keys("123456789")

    def fill_valid_school_contact_email(self):
        self.driver.find_element(*self.school_contact_email).send_keys(random_email())

    def fill_special_school_contact_email(self):
        self.driver.find_element(*self.school_contact_email).send_keys(random_email_special())

    def fill_no_domain_school_contact_email(self):
        self.driver.find_element(*self.school_contact_email).send_keys(random_email_no_domain())

    def fill_double_at_school_contact_email(self):
        self.driver.find_element(*self.school_contact_email).send_keys(random_email_double_at())

    def fill_without_at_school_contact_email(self):
        self.driver.find_element(*self.school_contact_email).send_keys(random_email_without_at())

    def accept_school_terms(self):
        self.driver.find_element(*self.school_terms_accepted).click()

    def accept_school_gdpr(self):
        self.driver.find_element(*self.school_gdpr_accepted).click()

    def click_on_voivodeship(self):
        self.driver.find_element(*self.school_voivodeship).click()

    def choose_voivodeship(self):
        self.driver.find_element(*self.silesian_voivodeship).click()

    def fill_invalid_school_contact_phone(self):
        self.driver.find_element(*self.school_contact_phone).send_keys("0123456789")

    def is_request_sent(self):
        try:
            element = self.driver.find_element(By.CLASS_NAME, "modal-content animated-in")
            if element.is_displayed():
                return AssertionError
        except NoSuchElementException:
            return True

    def submit_school_registration(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Wyślij wniosek')]"))).click()

    def assert_input_length(self):
        element = self.driver.find_element(*self.school_postal_code)
        value = element.get_attribute("value")
        actual_length = len(value)
        if actual_length == 6:
            return True
        else:
            return False

    def school_error(self):
        if visibility_of_element_located(self.school_error_message):
            return False
        else:
            return True

    def go_to_suggestions(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_button)).click()

    def valid_suggestion_message(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_input)).send_keys("Wow! cool app!")

    def test_admin_suggestion_message(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.suggestions_input)).send_keys("Testing")

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

    def go_to_login(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def go_to_language(self):
        button = self.driver.wait.until(EC.presence_of_element_located(self.language_button))
        self.driver.execute_script("arguments[0].click();", button)

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
