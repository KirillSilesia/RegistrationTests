from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import conftest

class WaitHandler:
    def __init__(self, driver, timeout=15):
        self.wait = WebDriverWait(driver, timeout)

    def until(self, condition):
        return self.wait.until(condition)