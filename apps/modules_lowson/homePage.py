from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, url="https://www.lawsonproducts.com/"):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.NAME, "username").send_keys("satish.kundem@gmail.com")
        self.driver.find_element(By.ID, "okta-signin-password").send_keys("945d8QN4uUQDWwd")
        self.driver.find_element(By.XPATH, "//*[@value='Sign In']").click()
        time.sleep(5)



