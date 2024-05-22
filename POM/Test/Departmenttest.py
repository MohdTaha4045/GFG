import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from ..Page.AddDeparment import AddDepartment

@pytest.fixture()
def driver():
    river = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver()
    driver.close()
    driver.quit()

def test_Department(driver):
    dep_add = AddDepartment(driver)
    dep_add.open_page("https://hrms-test.geeksforgeeks.org/department")
    dep_add.open_department()
    dep_add.add_department()
    time.sleep(20)

