from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    txt_customerId_name = "customerId"
    txt_password_name = "password"
    btn_login_xpath = "//button[text()='Log In']"
    # msg_myaccount_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setcustomerId(self, customerId):
        self.driver.find_element(By.NAME,self.txt_customerId_name).send_keys(customerId)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
