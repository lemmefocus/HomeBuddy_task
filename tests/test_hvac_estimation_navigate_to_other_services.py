import pytest

from constants import TestVariables, DirNames
from selenium.webdriver.common.by import By
from ui_pages import pages
from actions import *
from ui_pages.pages import PageQuestionnaireHVAC, PageHVAC, PageSorrySeeYouGo, PageHome


def prepare_data():
    return [("replacement_installation", "air_conditioner", "less_five_years", "commercial_modular"),
              ("not_sure", "air_conditioner", "not_sure", "apartment_building"),
              ("repair", "", "", "")]


@pytest.mark.parametrize(('project_type', 'equipment_item', 'equipment_old', 'property_type'), prepare_data())
def test_hvac_estimation_navigate_to_other_services(driver, project_type, equipment_item, equipment_old, property_type):
    driver.get(PageHVAC.url)

    # Fill out with ZIP code
    wait_until_element_appear(driver, By.ID, PageHVAC.input_zip_code_header)
    send_keys(driver, By.ID, pages.PageHVAC.input_zip_code_header, TestVariables.ZIP_CODE_VALUE)
    get_estimate_buttons = driver.find_elements(By.CLASS_NAME, PageHVAC.button_get_estimate)
    if get_estimate_buttons:
        get_estimate_buttons[0].click()

    # 'Sorry to see toy go page' steps according to different prepare data
    click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.ProjectTypes, project_type))
    if project_type == DirNames.REPAIR:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_no)
        wait_until_element_appear(driver, By.XPATH, PageSorrySeeYouGo.text_sorry)
        wait_until_element_appear(driver, By.XPATH, PageSorrySeeYouGo.text_check_out)
    else:
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next)

        click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.EquipmentItems, equipment_item))
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

        click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.EquipmentOld, equipment_old))
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_next, sleep_duration=0.5)

        click_element(driver, By.XPATH, getattr(PageQuestionnaireHVAC.PropertyTypes, property_type))
        click_element(driver, By.CSS_SELECTOR, PageQuestionnaireHVAC.button_no)

        wait_until_element_appear(driver, By.XPATH, PageSorrySeeYouGo.text_sorry)
        wait_until_element_appear(driver, By.XPATH, PageSorrySeeYouGo.text_check_out)

    # Checking on home page
    click_element(driver, By.CSS_SELECTOR, PageSorrySeeYouGo.button_homepage)
    wait_until_element_appear(driver, By.XPATH, PageHome.button_find)
    assert driver.current_url == PageHome.url
    assert driver.title == PageHome.title

