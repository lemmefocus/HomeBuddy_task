import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--deny-permission-prompts')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()
