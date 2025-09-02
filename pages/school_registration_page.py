from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from utils.global_utils import *
from generators.email_generators import *
from generators.nip_generators import *

class SchoolRegistrationPage:

    def __init__(self, driver):
        self.driver = driver
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
