from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import USER_NAME,PASSWORD,LOG_IN


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_field = USER_NAME
        self.password_field = PASSWORD
        self.login_button = LOG_IN
    def enter_username(self, username: str):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_success(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))
            return False
        except:
            return True
        
    def set_placeholder(self,locator,placeholder):
        input_element = self.driver.find_element(*locator)
        self.driver.execute_script(f"arguments[0].setAttribute('placeholder', '{placeholder}')", input_element)
        