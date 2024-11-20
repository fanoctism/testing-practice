from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_invalid_location(driver):
    driver.get("https://www.bbc.com/weather")
    try:
        # Try to find a non-existing element for testing error handling
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".non-existing-element"))
        )
    except TimeoutException:
        print("Timeout: Element not found within time limit")
        driver.save_screenshot("error_screenshot.png")
