from selenium.webdriver.common.by import By
import time

class Electrical:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_elecrical(self):
        self.driver.find_element(By.XPATH, "//a[@id='ip8zy-4-88-3-69']").click()
        time.sleep(2)
