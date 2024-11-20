from selenium.webdriver.common.by import By


def test_navigation_to_weather(driver):
    driver.get("https://www.bbc.com/weather")
    weather_button = driver.find_element(By.LINK_TEXT, "Weather")
    weather_button.click()
    assert "Weather" in driver.title
