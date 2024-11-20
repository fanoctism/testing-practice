from selenium.webdriver.common.action_chains import ActionChains

def dismiss_popup(driver):
    """
    Dismisses popups if present.
    """
    try:
        popup = driver.find_element(By.CLASS_NAME, "popup-class-name")  # Replace with actual popup class
        ActionChains(driver).move_to_element(popup).click().perform()
    except Exception:
        pass
