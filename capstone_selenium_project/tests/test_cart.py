from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_product_to_cart():

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
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "search_product"))
    )

    # Search Blue Top
    search_box.send_keys("Blue Top")

    # Click Search
    driver.find_element(By.ID, "submit_search").click()

    # Wait for Blue Top
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='productinfo text-center']/p[text()='Blue Top']")
        )
    )

    # Find Add to Cart button
    add_to_cart = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='productinfo text-center']/p[text()='Blue Top']/ancestor::div[contains(@class,'product-image-wrapper')]//a[contains(@class,'add-to-cart')]"
            )
        )
    )

    # Scroll to Add to Cart button
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_to_cart
    )

    time.sleep(1)

    # JavaScript click
    driver.execute_script(
        "arguments[0].click();",
        add_to_cart
    )

    time.sleep(2)

    # Click View Cart
    view_cart = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//u[text()='View Cart']")
        )
    )
    view_cart.click()

    # Wait for cart
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//td[@class='cart_description']//a")
        )
    )

    # Verify product
    assert product_name.text == "Blue Top"

    print("Product successfully added to cart!")

    time.sleep(2)

    driver.quit()