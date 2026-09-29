from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_verify_cart_details():

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

    # Add product to cart
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

    # Product name
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//td[@class='cart_description']//a")
        )
    )

    # Quantity
    quantity = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//td[@class='cart_quantity']//button")
        )
    )

    # Price
    price = driver.find_element(
        By.XPATH, "//td[@class='cart_price']/p"
    )

    # Total price
    total_price = driver.find_element(
        By.XPATH, "//td[@class='cart_total']/p"
    )

    # Print cart details
    print("Product:", product_name.text)
    print("Quantity:", quantity.text)
    print("Price:", price.text)
    print("Total:", total_price.text)

    # Verify details
    assert product_name.text == "Blue Top"
    assert quantity.text == "1"
    assert price.text != ""
    assert total_price.text != ""

    print("Cart details verified successfully!")

    time.sleep(2)

    driver.quit()