from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_update_quantity():

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

    # Search Blue Top
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

    # Find Add to Cart
    add_to_cart = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='productinfo text-center']/p[text()='Blue Top']/ancestor::div[contains(@class,'product-image-wrapper')]//a[contains(@class,'add-to-cart')]"
            )
        )
    )

    # Scroll to product
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_to_cart
    )

    time.sleep(1)

    # Click Add to Cart using JavaScript
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

    # Wait for quantity field
    quantity = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[@class='cart_quantity']//button")
        )
    )

    # Verify initial quantity
    assert quantity.text == "1"

    print("Initial quantity is 1")

    time.sleep(1)

    # Increase quantity using Add to Cart again
    driver.get("https://automationexercise.com/products")

    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "search_product"))
    )

    search_box.send_keys("Blue Top")

    driver.find_element(By.ID, "submit_search").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='productinfo text-center']/p[text()='Blue Top']")
        )
    )

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

    # Check updated quantity
    quantity = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[@class='cart_quantity']//button")
        )
    )

    print("Updated quantity:", quantity.text)

    assert quantity.text == "2"

    print("Quantity updated successfully!")

    time.sleep(2)

    driver.quit()