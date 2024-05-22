import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XLUtils


class Login:
    logout_xpath1 = "//a[@href = 'https://adevtest.geeksforgeeks.org/logout.php/?to=https://adevtest.geeksforgeeks.org/']"
    logout_xpath2 = "//i[text() = 'logout']"
    usernameField_xpath = "//input[@placeholder='Username or email']"
    passwordField_xpath = "//input[@id='password']"
    signIn_xpath = "//button[text()='Sign In']"
    remindMeLater_xpath = "//div[@id='lower_section_text']"
    path = "/home/administrator/PycharmProjects/pythonSelenium/testData/loginCredentials.xlsx"

    def __init__(self,driver):  #here we initial the driver ,__init__ is a special method in Python classes that serves as the constructor for the class.
        self.passwordField_id = None
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH,(self.usernameField_xpath)).clear()
        self.driver.find_element(By.XPATH,(self.usernameField_xpath)).send_keys(username)
        time.sleep(1)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,(self.passwordField_xpath)).clear()
        self.driver.find_element(By.XPATH,(self.passwordField_xpath)).send_keys(password)
        time.sleep(1)

    def clickSignIn(self):
        self.driver.find_element(By.XPATH,(self.signIn_xpath)).click()
        time.sleep(10)

    def skipRoadBloack(self):
        self.driver.find_element(By.XPATH,(self.remindMeLater_xpath)).click()
        # time.sleep(10)

    def DDT(self):
        rows = XLUtils.getRowCount(self.path, 'Sheet1')

        for r in range(2, rows + 1):
            username = XLUtils.readData(self.path, "Sheet1", r, 1)
            password = XLUtils.readData(self.path, "Sheet1", r, 2)
            expectedTitle = username + " | GeeksforGeeks Profile"

            self.driver.find_element(By.XPATH, (self.usernameField_xpath)).send_keys(username)
            self.driver.find_element(By.XPATH, (self.passwordField_xpath)).send_keys(password)
            self.driver.find_element(By.XPATH, (self.remindMeLater_xpath)).click()
            self.driver.find_element(By.XPATH, (self.remindMeLater_xpath)).click()

            if driver.title == expectedtitle:
                print("test is passed")
                if act_title == "username | GeeksforGeeks Profile":
                    assert True
                    self.driver.close()
                else:
                    print("test is failed")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_login_DDT.png")
                    assert False
                    self.driver.close()

            driver.find_element(By.XPATH, ("//a[@href = 'https://adevtest.geeksforgeeks.org/logout.php/?to=https://adevtest.geeksforgeeks.org/']")).click()
