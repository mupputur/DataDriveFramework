from selenium.webdriver.common.by import By
import time

class Product:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_product(self):
        self.driver.find_element(By.XPATH, "//li[@class='categoryContainer']/a[1]").click()
        time.sleep(3)
