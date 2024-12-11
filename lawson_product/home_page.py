from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, url="https://www.lawsonproducts.com/"):

        chromedriver_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\code_repository\\automation-framework\\lawson_product\\driver\\chromedriver.exe"

        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.NAME, "username").send_keys("kumarpavan79015@gmail.com")
        self.driver.find_element(By.ID, "okta-signin-password").send_keys("Pawanloki6")
        self.driver.find_element(By.XPATH, "//*[@value='Sign In']").click()
        time.sleep(5)



