from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://adevtest.geeksforgeeks.org/")
print(driver.title)
driver.find_element(By.XPATH,"")
driver.find_element_by_id("luser").send_keys("mohdt2nrm")
driver.find_element_by_id("password").send_keys("Taha@Geeks123#")
driver.find_element_by_xpath("//button[text()='Sign In']").click()

