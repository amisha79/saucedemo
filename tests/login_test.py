import time
import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.locators import USER_NAME


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    #login_page.enter_username('validusername')
    #login_page.enter_password('validpassword')
    login_page.click_login()
    assert login_page.is_success() is True

    
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('validusername')
    login_page.enter_password('validpassword')
    login_page.click_login()
    assert login_page.is_success() is False

def test_empty_pw_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('validusername')
    login_page.enter_password('')
    login_page.click_login()
    assert login_page.is_success() is False

def test_empty_user_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('')
    login_page.enter_password('validpassword')
    login_page.click_login()
    assert login_page.is_success() is False

def test_diff_user_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('error_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()
    assert login_page.is_success() is True
#is vissible

#placeholder change
def test_set_placeholder(driver):
    login_page=LoginPage(driver)
    login_page.set_placeholder(USER_NAME,'amisha')
    time.sleep(20)


