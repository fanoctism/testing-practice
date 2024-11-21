from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_browser():
    # Create and return a new Chrome browser instance
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: For headless mode, useful for CI/CD pipelines
    options.add_argument('--no-sandbox')  # Prevents the browser from hanging on certain environments

    # Initialize Chrome WebDriver with the correct Service object
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver
