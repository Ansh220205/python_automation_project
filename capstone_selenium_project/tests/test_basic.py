from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/")

driver.maximize_window()

print("Title:", driver.title)

time.sleep(5)

driver.quit()