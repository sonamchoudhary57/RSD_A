from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage():
    tab_username_xpath = "//div[contains(text(),'sonam')]"
    btn_addproperty_xpath = "(//button[text()='Add Property'])[2]"
    txt_name_name = "Name"
    txt_phone_name = "PhoneNumber"
    btn_save_xpath = "//button[text()='save']"


    def __init__(self, driver):
        self.driver = driver
    
    def clickusername(self):
        self.driver.find_element(By.XPATH,self.tab_username_xpath).click()

    def clickaddproperty(self):
        self.driver.find_element(By.XPATH,self.btn_addproperty_xpath).click()
    
    def setname(self, name):
        self.driver.find_element(By.NAME,self.txt_name_name).send_keys(name)

    def setphone(self, phone):
        self.driver.find_element(By.NAME,self.txt_phone_name).send_keys(phone)

    def clicksave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()    
