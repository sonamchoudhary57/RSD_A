import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module", autouse=True)

def setup():

    driver = webdriver.Edge()
    driver.get("http://3.80.90.25:3008/#/adminlogin")
    driver.maximize_window()

    

    return driver