import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.LoginPage import Login

class TestLogin:
    baseURL = "https://adevtest.geeksforgeeks.org/"
    username = "mohdt2nrm"
    password = "Taha@Geeks123#"

    def test_home_page_title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(self.baseURL)
        act_title = driver.title
        driver.close()

        assert act_title == "Login GeeksforGeeks"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_sign_in()
        act_title = self.driver.title
        self.driver.close()

        assert act_title == "mohdt2nrm | GeeksforGeeks Profile"
