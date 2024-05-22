import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.LoginPage import Login

class Test_001_Login:
   baseURL = "https://adevtest.geeksforgeeks.org/"
   username = "mohdt2nrm"
   password = "Taha@Geeks123#"

   def test_homePageTitle(self,setup):
        #self.driver = webdriver.chrome()

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title == "Luogin GeekforGeeks" :
            assert True
            self.driver.close()

        else:
            # self.driver.save_screenshot()
            self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
            self.driver.close()

   def test_login(self,setup):
       #self.driver = webdriver.chrome()

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        self.lp.skipRoadBloack()
        act_title = self.driver.title
        print("The act_title is : "+act_title)
        time.sleep(2)
        if act_title == "mohdt2nrm | GeeksforGeeks Profile":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False
            self.driver.close()


   def test_login(self,setup):
       #self.driver = webdriver.chrome()

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)












        self.lp.DDT()
