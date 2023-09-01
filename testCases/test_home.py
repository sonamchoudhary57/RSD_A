import pytest
import os
import sys
# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append('../')
# from ..pageObjects.LoginPageObject import LoginPage
from selenium import webdriver
from test_login import TestLogin
from pageObjects.HomePageObject import HomePage
from selenium.webdriver.common.by import By
from conftest import setup

class TestHome:

    def test_home(self, setup):

        self.driver = setup
        self.lp = TestLogin(self)
        self.hp = HomePage(self.driver)
        self.hp.clickusername()
        self.hp.clickaddproperty()
        self.hp.setname("rohan")
        self.hp.setphone("1234567890")
        self.hp.clicksave()
        # self.driver.close()

