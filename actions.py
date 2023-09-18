import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

WAIT_FOR_ELEMENT_SECONDS = 10


def click_element(driver, by, value, timeout=WAIT_FOR_ELEMENT_SECONDS, sleep_duration=0):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.element_to_be_clickable((by, value))
        )
        element.click()
        time.sleep(sleep_duration)
    except Exception as error:
        raise f"Failed to click on element: {error}"


def send_keys(driver, by, value, text, timeout=WAIT_FOR_ELEMENT_SECONDS):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, value))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().send_keys(text).perform()
    except Exception as error:
        raise f"Failed to send keys to element: {error}"

    return element


def wait_until_element_appear(driver, by: str, value: str, timeout=WAIT_FOR_ELEMENT_SECONDS, attempt: int = 0, max_attempts: int = 3):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, value)))
        ActionChains(driver).move_to_element(element).perform()
    except StaleElementReferenceException as error:
        if attempt < max_attempts:
            return wait_until_element_appear(driver, by, value, timeout, attempt=attempt + 1, max_attempts=max_attempts)
        else:
            raise Exception(f"Failed to detect an element: {error}")

    return element
