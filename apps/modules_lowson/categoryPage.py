from selenium.webdriver.common.by import By
import time
import json

class CategoryPage:
    def __init__(self, driver):
        self.driver = driver
    def navigate_to_category(self):
        product = self.driver.find_elements(By.XPATH, "//div[@id='products']//li")
        l_product = len(product)
        print(l_product)

        for i in range(1, l_product):
            cells = self.driver.find_element(By.XPATH, f"//div[@id='products']//li[{i}]")
            name = cells.text
            l = len(name)
            print(name)
            cells.click()
            time.sleep(2)
            titles = self.driver.find_elements(By.XPATH, "//div[@class='grid-row product-item product-item--gallery-view']/div/div[contains(@class,' hidden')]")
            print("No.Of " + name + ":" + str(len(titles)))
            for inner_battery in titles:
                d = inner_battery.get_attribute("data-gtm-model")
                data = json.loads(d)
                id_value = data["id"]
                name_value = data["name"]
                print("ID:", id_value)
                print("NAME:", name_value)
                print(" ")
            print(" ")
            self.driver.back()
            time.sleep(2)
