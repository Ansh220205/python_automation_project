from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


def test_search_product():

    # Read test data from JSON
    with open("test_data/test_data.json", "r") as file:
        data = json.load(file)

    product_name = data["product_name"]

    driver = webdriver.Chrome()

    # Open AutomationExercise
    driver.get("https://automationexercise.com/")

    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # Click Products
    products = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Products')]")
        )
    )
    products.click()

    # Wait for search box
    wait.until(
        EC.presence_of_element_located((By.ID, "search_product"))
    )

    # Search product from JSON
    search_box = driver.find_element(By.ID, "search_product")
    search_box.send_keys(product_name)

    # Click search
    driver.find_element(By.ID, "submit_search").click()

    # Wait for search result
    result = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='productinfo text-center']/p")
        )
    )

    # Verify product
    assert result.text == product_name

    print("Product search successful!")

    time.sleep(2)

    driver.quit()