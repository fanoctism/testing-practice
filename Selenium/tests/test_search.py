from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_bbc_weather_search(driver):
    driver.get("https://www.bbc.com/weather")
    try:
        location_name = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID, "wr-location-name-id"))
        )
        print(location_name.text)
    except TimeoutException:
        print("Timeout: Location name element not found within time limit")
        driver.save_screenshot("screenshot.png")
