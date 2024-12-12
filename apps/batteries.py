from selenium.webdriver.common.by import By
import time

class Batteries:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_battery(self):
        self.driver.find_element(By.XPATH, "(//section[contains(@class,'page-content page-content--has-sidebar')]//li[1])[2]").click()
        time.sleep(3)