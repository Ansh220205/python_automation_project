from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_alert_handling():

    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com/")

    driver.maximize_window()

    time.sleep(2)

    # Open Contact Us page
    driver.find_element(
        By.XPATH, "//a[contains(text(),'Contact us')]"
    ).click()

    time.sleep(2)

    # Verify Contact Us page
    heading = driver.find_element(
        By.XPATH, "//h2[contains(text(),'Get In Touch')]"
    )

    assert heading.is_displayed()

    print("Contact Us page opened successfully!")

    driver.quit()