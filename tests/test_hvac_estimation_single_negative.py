import random
from constants import TestVariables
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from ui_pages import pages
from actions import *
from ui_pages.pages import PageQuestionnaireHVAC, PageThankYou, PageHVAC


def test_hvac_estimation_single_negative(driver):
    driver.get(PageHVAC.url)

    # Fill out with ZIP code
    wait_until_element_appear(driver, By.ID, PageHVAC.input_zip_code_header)
    get_estimate_buttons = driver.find_elements(By.CLASS_NAME, PageHVAC.button_get_estimate)
    if get_estimate_buttons:
        get_estimate_buttons[0].click()

    wait_until_element_appear(driver, By.XPATH, PageHVAC.error_no_zip_code)
    send_keys(driver, By.ID, pages.PageHVAC.input_zip_code_header, TestVariables.ZIP_CODE_VALUE)
    get_estimate_buttons[0].click()

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.ProjectTypes.replacement_installation)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.EquipmentItems.heat_pump, sleep_duration=0.5)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.SystemType.oil)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.EquipmentOld.not_sure)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.PropertyTypes.detached_row_house)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    input_field = send_keys(driver, By.ID, PageQuestionnaireHVAC.HouseSquareFeet.input_square_feet,
              TestVariables.ERROR)

    assert not next_button.is_enabled()
    wait_until_element_appear(driver, By.XPATH, PageQuestionnaireHVAC.HouseSquareFeet.error_numbers_only)
    input_field.clear()
    send_keys(driver, By.ID, PageQuestionnaireHVAC.HouseSquareFeet.input_square_feet,
                            TestVariables.SQUARE_FEET_VALUE)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    next_button = wait_until_element_appear(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    assert not next_button.is_enabled()

    click_element(driver, By.XPATH, PageQuestionnaireHVAC.HomeownerAuthorized.button_yes, sleep_duration=0.5)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)
    wait_until_element_appear(driver, By.XPATH, PageQuestionnaireHVAC.PrepareEstimateData.error_full_name)
    wait_until_element_appear(driver, By.XPATH, PageQuestionnaireHVAC.PrepareEstimateData.error_email)

    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PrepareEstimateData.input_full_name, TestVariables.FULL_NAME)
    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PrepareEstimateData.input_email, TestVariables.EMAIL)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    wait_until_element_appear(driver, By.ID, pages.PageQuestionnaireHVAC.PhoneNumber.input_phone_number)
    click_element(driver, By.CSS_SELECTOR, pages.PageQuestionnaireHVAC.PhoneNumber.button_submit_request)

    wait_until_element_appear(driver, By.XPATH, PageQuestionnaireHVAC.PhoneNumber.error_phone_number)

    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PhoneNumber.input_phone_number,
              str([random.randint(1, 9) for _ in range(11)]))
    click_element(driver, By.CSS_SELECTOR, pages.PageQuestionnaireHVAC.PhoneNumber.button_submit_request)

    # Checking verify phone number page
    try:
        wait_until_element_appear(driver, By.XPATH, pages.PageQuestionnaireHVAC.VeryfyPhoneNumber.text_confirm,
                                  max_attempts=0)
        click_element(driver, By.CSS_SELECTOR, pages.PageQuestionnaireHVAC.VeryfyPhoneNumber.button_correct,
                      sleep_duration=0.5)
    except TimeoutException:
        print("Verify number page is skipped")

    # Checking the presence of the 'thank you' page
    wait_until_element_appear(driver, By.XPATH,
                              PageThankYou().get_text_thank_you_locator(TestVariables.FULL_NAME.split()[0]),
                              max_attempts=3)

    assert driver.current_url == PageThankYou.url



