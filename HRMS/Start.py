from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def main():
    # Setting up Chrome driver
    service = Service('./drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait

    try:
        # Navigating to the website
        driver.get("https://authtest.geeksforgeeks.org/")
        time.sleep(3)

        # Clicking on the Sign Up button
        signUp = driver.find_element(By.XPATH, "//label[text()='Sign Up']")
        signUp.click()
        time.sleep(3)

        # Entering email
        email = driver.find_element(By.ID, "email")
        email.send_keys("Mohdtaha4045@gmail.com ")
        time.sleep(3)

        # Entering password
        password = driver.find_element(By.ID, "reg-password")
        password.send_keys("Taha@Geeks12345")
        time.sleep(3)

        # Entering institution
        institution = driver.find_element(By.ID, "organization")
        institution.send_keys("Allenhouse")
        time.sleep(3)

        # Pressing down arrow to select from dropdown
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(3)

        """
        # Switching to reCAPTCHA iframe
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        driver.switch_to.frame(iframe)

        # Manually solve reCAPTCHA or implement custom solution

        # Switching back to default content
        driver.switch_to.default_content()
        """

        """
        # Clicking on the captcha
        captcha = driver.find_element(By.XPATH, "//div[@class='login-modal-div']")
        captcha.click()

        # Clicking on the captcha solver button
        captchaSolver = driver.find_element(By.ID, "solver-button")
        captchaSolver.click()
        time.sleep(3)
        """

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Closing the browser window
        driver.quit()

if __name__ == "__main__":
    main()
