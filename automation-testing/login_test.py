from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH
driver.get("https://www.saucedemo.com/")  # Navigate to the website

try:
    # Locate and interact with elements
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Input credentials and submit
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for the page to load
    time.sleep(2)

    # Validate login
    if "Products" in driver.page_source:
        print("Login successful!")
    else:
        print("Login failed!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()