from selenium.webdriver.common.by import By
import time


class ElectricalTool:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_electrical_tool(self):
        self.driver.find_element(By.XPATH,"//section[contains(@class,'page-content page-content--has-sidebar')]//li[7]").click()
        time.sleep(3)