import pytest
import os
import sys
# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append('../')
# from ..pageObjects.LoginPageObject import LoginPage
from pageObjects.LoginPageObject import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import setup

class TestLogin:

    def test_login(self, setup):
        
        self.driver = setup
        # self.driver.get("http://3.80.90.25:3008/#/adminlogin")
        # self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setcustomerId("Sonam")
        self.lp.setPassword("testing")
        self.lp.clickLogin()
        self.act_title=self.driver.title
        # self.driver.close()
        assert self.act_title == "Radiant RSD Portal"


   
