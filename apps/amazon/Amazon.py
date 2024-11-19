#Open the amazon webpage and print the number of slides and their text


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to ChromeDriver
s = Service(executable_path="C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Open Amazon website
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(3)

#find_elements to get all elements with the specified class
slides = driver.find_elements(By.XPATH, "//*[@class='a-carousel-card' and contains (@role,'listitem')]//img")

# print number of the slides
print("Number of slides:", len(slides))
for slide in slides:
    slide_text = slide.get_attribute("alt")
    print("slide:",slide_text)

time.sleep(3)
driver.quit()
