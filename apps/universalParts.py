from selenium.webdriver.common.by import By
import time

class UniversalParts:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_universal_parts(self):
        self.driver.find_element(By.XPATH,"//section[contains(@class,'page-content page-content--has-sidebar')]//li[7]").click()
        time.sleep(2)