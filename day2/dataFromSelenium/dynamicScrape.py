from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Path to chromedriver relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, "chromedriver.exe")

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/js/")
time.sleep(3)

print("Page title:", driver.title)

quotes = driver.find_elements(By.CLASS_NAME, "text")

for q in quotes:
    print(q.text)

driver.quit()
