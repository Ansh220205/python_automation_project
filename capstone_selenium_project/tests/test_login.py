from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():

    driver = webdriver.Chrome()

    # Open website
    driver.get("https://automationexercise.com/")

    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # Click Signup / Login
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Signup / Login')]")
        )
    )

    login_button.click()

    # Wait for login form
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Login to your account')]")
        )
    )

    # Enter email
    email = driver.find_element(
        By.XPATH, "//input[@data-qa='login-email']"
    )

    email.send_keys("YOUR_EMAIL")

    # Enter password
    password = driver.find_element(
        By.XPATH, "//input[@data-qa='login-password']"
    )

    password.send_keys("YOUR_PASSWORD")

    # Click Login
    driver.find_element(
        By.XPATH, "//button[@data-qa='login-button']"
    ).click()

    # Wait for logout button
    logout = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Logout')]")
        )
    )

    # Verify successful login
    assert logout.is_displayed()

    print("Login successful!")

    time.sleep(2)

    driver.quit()