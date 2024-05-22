from google.protobuf.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://adevtest.geeksforgeeks.org/")
path = "/home/administrator/PycharmProjects/pythonSelenium/testData/loginCredentials.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)
    expectedtitle = username + " | GeeksforGeeks Profile"

    driver.find_element(By.XPATH, ("//input[@placeholder='Username or email']")).send_keys(username)
    driver.find_element(By.XPATH, ("//input[@id='password']")).send_keys(password)
    driver.find_element(By.XPATH, ("//button[text()='Sign In']")).click()
    driver.find_element(By.XPATH, ("//div[@id='lower_section_text']")).click()

    if driver.title == expectedtitle:
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")

    else:
        print("test is fail")
        XLUtils.writeData(path, "Sheet1", r, 3, "test Failed")

    driver.find_element(By.XPATH, ("//a[@href = 'https://adevtest.geeksforgeeks.org/logout.php/?to=https://adevtest.geeksforgeeks.org/']")).click()

