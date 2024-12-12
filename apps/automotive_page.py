from selenium.webdriver.common.by import By
import time

class AutomotivePage:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_automotive(self):
        self.driver.find_element(By.XPATH,"//a[@id='id9mog-4-88-3-69']").click()
        time.sleep(2)