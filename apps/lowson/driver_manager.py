from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DriverManager:


    def __init__(self):
        self.driver = None
        self.url = "https://www.lawsonproducts.com/"
        self.initilize_driver()

    def initilize_driver(self):
        try:
            # TODO:  Fix the driver initilzation by providing relative path from the dependecies 
            self.driver = webdriver.Chrome(executable_path=r"C:\\Users\\91998\\Documents\\GitRepos\\automation-framework\\dependencies\\chromedriver.exe") 
            self.driver.maximize_window()
            self.driver.get(url)
        except Exception as e:
            print(f"Error: {str(e)}")
            raise "Fail to initilize driver or Unable to launch the app"

# The below lines is to test this module
# this won't run when we import this module into another file 
if __name__ == "__main__":
    driver = DriverManager()
    
