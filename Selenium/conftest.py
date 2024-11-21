import pytest
from browser_setup import create_browser


@pytest.fixture
def driver():
    # Setup the WebDriver for tests
    driver = create_browser()
    yield driver
    driver.quit()  # Clean up the WebDriver after each test
