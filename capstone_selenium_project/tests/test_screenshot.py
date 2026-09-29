from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def test_capture_screenshot():

    driver = webdriver.Chrome()

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

    # Search product
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "search_product"))
    )

    search_box.send_keys("Blue Top")

    driver.find_element(By.ID, "submit_search").click()

    # Wait for product
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='productinfo text-center']/p[text()='Blue Top']")
        )
    )

    # Add to cart
    add_to_cart = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='productinfo text-center']/p[text()='Blue Top']/ancestor::div[contains(@class,'product-image-wrapper')]//a[contains(@class,'add-to-cart')]"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_to_cart
    )

    driver.execute_script(
        "arguments[0].click();",
        add_to_cart
    )

    time.sleep(2)

    # View Cart
    view_cart = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//u[text()='View Cart']")
        )
    )

    view_cart.click()

    # Wait for cart
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//td[@class='cart_description']//a")
        )
    )

    # Create screenshots folder if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)

    # Capture screenshot
    driver.save_screenshot("screenshots/cart_details.png")

    print("Screenshot captured successfully!")

    time.sleep(2)

    driver.quit()