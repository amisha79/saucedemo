import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import logging
from pages.login import LoginPage

logger = logging.getLogger('my_logger')

# Set the log level
logger.setLevel(logging.DEBUG)

def test_hover_product(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()
    if login_page.is_success():
        logger.info("sucessfully logged-in")
    time.sleep(3)
    actions = ActionChains(driver)
    element_1 = driver.find_element(By.ID, "item_4_title_link")
    # Hover over the element
    actions.move_to_element(element_1).perform()
    time.sleep(3)
    element_2 = driver.find_element(By.ID, "item_2_title_link")
    actions.move_to_element(element_2).perform()
    time.sleep(3)
    actions.move_to_element(element_1).perform()
    time.sleep(5)
    

    
    