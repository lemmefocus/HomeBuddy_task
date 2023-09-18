import random
import pytest

import constants
from constants import TestVariables, DirNames
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from itertools import product
from ui_pages import pages
from actions import *
from ui_pages.pages import PageQuestionnaireHVAC, PageThankYou, PageHVAC


def prepare_data():
    project_types = [item for item in dir(PageQuestionnaireHVAC.ProjectTypes) if not item.startswith("__")]
    equipment_items = [item for item in dir(PageQuestionnaireHVAC.EquipmentItems) if not item.startswith("__")]
    system_types = [item for item in dir(PageQuestionnaireHVAC.SystemType) if not item.startswith("__")]
    equipment_old = [item for item in dir(PageQuestionnaireHVAC.EquipmentOld) if not item.startswith("__")]
    property_types = [item for item in dir(PageQuestionnaireHVAC.PropertyTypes) if not item.startswith("__")]
    house_square_feet = [item for item in dir(PageQuestionnaireHVAC.HouseSquareFeet) if not item.startswith("__") and not item.startswith("error")]
    homeowner_authorized = [item for item in dir(PageQuestionnaireHVAC.HomeownerAuthorized) if
                            not item.startswith("__")]

    # Create all possible combinations of the attribute names
    all_combinations = list(product(
        project_types, equipment_items, system_types, equipment_old,
        property_types, house_square_feet, homeowner_authorized
    ))

    return all_combinations


@pytest.mark.parametrize(('project_type', 'equipment_item', 'system_type', 'equipment_old', 'property_type',
                          'house_square_feet', 'homeowner_authorized'), prepare_data())
def test_hvac_estimation_positive(driver, project_type, equipment_item, system_type, equipment_old, property_type,
                         house_square_feet,
                         homeowner_authorized):
    driver.get(PageHVAC.url)

    # Fill out with ZIP code
    wait_until_element_appear(driver, By.ID, PageHVAC.input_zip_code_header)
    send_keys(driver, By.ID, pages.PageHVAC.input_zip_code_header, TestVariables.ZIP_CODE_VALUE)
    get_estimate_buttons = driver.find_elements(By.CLASS_NAME, PageHVAC.button_get_estimate)
    if get_estimate_buttons:
        get_estimate_buttons[0].click()

    # Checking on project type
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.ProjectTypes, project_type))
    if project_type == DirNames.REPAIR:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_yes, sleep_duration=0.5)
    else:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    # Checking in equipment items
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.EquipmentItems, equipment_item), sleep_duration=0.5)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

    # Checking on system type
    if equipment_item != DirNames.AIR_CONDITIONER:
        click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.SystemType, system_type))
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    # Checking on equipment old
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.EquipmentOld, equipment_old))
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    # Checking on property type
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.PropertyTypes, property_type))
    if property_type in [constants.DirNames.APARTMENT_BUILDING, constants.DirNames.COMMERCIAL_MODULAR]:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_yes)
    else:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    # Checking on house square feet or not sure
    if house_square_feet == DirNames.SQUARE_FEET:
        wait_until_element_appear(driver, By.ID, getattr(PageQuestionnaireHVAC.HouseSquareFeet, house_square_feet))
        send_keys(driver, By.ID, getattr(PageQuestionnaireHVAC.HouseSquareFeet, house_square_feet),
                  TestVariables.SQUARE_FEET_VALUE)
    else:
        click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.HouseSquareFeet, house_square_feet))
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    # Checking whether authorized or not
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.HomeownerAuthorized, homeowner_authorized))
    if homeowner_authorized.lower() == DirNames.YES:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)
    else:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_yes)

    # Checking on user data page
    wait_until_element_appear(driver, By.ID, pages.PageQuestionnaireHVAC.PrepareEstimateData.input_full_name)
    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PrepareEstimateData.input_full_name, TestVariables.FULL_NAME)
    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PrepareEstimateData.input_email, TestVariables.EMAIL)
    click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

    # Checking on phone number page
    wait_until_element_appear(driver, By.ID, pages.PageQuestionnaireHVAC.PhoneNumber.input_phone_number)
    send_keys(driver, By.ID, pages.PageQuestionnaireHVAC.PhoneNumber.input_phone_number,
              str([random.randint(1, 9) for _ in range(11)]))
    click_element(driver, By.CSS_SELECTOR, pages.PageQuestionnaireHVAC.PhoneNumber.button_submit_request)

    # Checking verify phone number page
    try:
        wait_until_element_appear(driver, By.XPATH, pages.PageQuestionnaireHVAC.VeryfyPhoneNumber.text_confirm,
                                  max_attempts=0)
        click_element(driver, By.CSS_SELECTOR, pages.PageQuestionnaireHVAC.VeryfyPhoneNumber.button_correct, sleep_duration=0.5)
    except TimeoutException:
        print("Verify number page is skipped")

    # Checking the presence of the 'thank you' page
    wait_until_element_appear(driver, By.XPATH,
                              PageThankYou().get_text_thank_you_locator(TestVariables.FULL_NAME.split()[0]),
                              max_attempts=3)

    assert driver.current_url == PageThankYou.url
