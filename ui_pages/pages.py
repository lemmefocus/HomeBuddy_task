class PageHome:
    url = "https://hb-autotests.stage.sirenltd.dev/"
    title = "HomeBuddy - Your Home Improvement Helper"
    button_find = "//span[contains(text(),'Let’s find out')]"


class PageHVAC:
    url = "https://hb-autotests.stage.sirenltd.dev/hvac"
    title = "HVAC - HomeBuddy"
    input_zip_code_header = "zipCode"
    input_zip_code_content = "zip_content1"
    input_zip_code_footer = "zip_footer1"
    button_get_estimate = "customButton.customButton_primary.customButton_large"
    error_no_zip_code = "//div[contains(text(),'A ZIP Code is required')]"


class PageQuestionnaireHVAC:
    button_next = "button[data-autotest-button-submit-next='']"
    button_no = "button[data-autotest-button-button-no='']"
    button_yes = "button[data-autotest-button-submit-yes='']"

    class ProjectTypes:
        repair = "//span[contains(text(),'Repair')]"
        not_sure = "//span[contains(text(),'Not sure')]"
        replacement_installation = "//span[contains(text(),'Replacement')]"

    class EquipmentItems:
        air_conditioner = "//span[contains(text(),'Air conditioner')]"
        central_heating = "//span[contains(text(),'Central heating')]"
        boiler_radiator = "//span[contains(text(),'Boiler/radiator')]"
        heat_pump = "//span[contains(text(),'Heat pump')]"
        water_heater = "//span[contains(text(),'Water heater')]"
        not_sure = "//span[contains(text(),'Not sure')]"

    class SystemType:
        gas = "//span[contains(text(),'Gas')]"
        electricity = "//span[contains(text(),'Electricity')]"
        propane = "//span[contains(text(),'Propane')]"
        oil = "//span[contains(text(),'Oil')]"
        not_sure = "//span[contains(text(),'Not sure')]"

    class EquipmentOld:
        less_five_years = "//span[contains(text(),'Less than 5')]"
        five_ten_years = "//span[contains(text(),'5 to 10')]"
        older_years = "//span[contains(text(),'Older than 10')]"
        not_sure = "//span[contains(text(),'Not sure')]"

    class PropertyTypes:
        detached_row_house = "//span[contains(text(),'Detached, semi-detached, row house')]"
        mobile_modular = "//span[contains(text(),'Mobile, modular, manufactured home')]"
        commercial_modular = "//span[contains(text(),'Commercial')]"
        apartment_building = "//span[contains(text(),'Apartment building')]"

    class HouseSquareFeet:
        input_square_feet = "squareFeet"
        checkbox_not_sure = "//div[contains(text(),'Not sure')]"

        # Error messages
        error_numbers_only = "//div[contains(text(),'Please use numbers only')]"

    class HomeownerAuthorized:
        button_yes = "//span[contains(text(),'Yes')]"
        button_no = "//span[contains(text(),'No')]"

    class PrepareEstimateData:
        input_full_name = "fullName"
        input_email = "email"

        # Error messages
        error_full_name = "//div[contains(text(),'Full name must be at least 3 characters.')]"
        error_email = "//div[contains(text(),'Email address must be at least 6 characters long.')]"

    class PhoneNumber:
        input_phone_number = "phoneNumber"
        button_submit_request = "button[data-autotest-button-submit-submit-my-request='']"

        # Error messages
        error_phone_number = "//div[contains(text(),'Phone number must be 10 digits long.')]"

    class VeryfyPhoneNumber:
        text_confirm = "//h4[contains(text(),'Please confirm your phone number.')]"
        input_phone_number = "phoneNumber"
        button_edit = "button[data-autotest-button-button-edit-phone-number='']"
        button_correct = "button[data-autotest-button-submit-phone-number-is-correct='']"


class PageThankYou:
    url = "https://hb-autotests.stage.sirenltd.dev/thank-you"
    title = "Thank you - HomeBuddy"

    @staticmethod
    def get_text_thank_you_locator(name):
        return f"//h4[contains(text(),'Thank you {name}, your contractor QA company will call soon!')]"


class PageSorrySeeYouGo:
    url = "https://hb-autotests.stage.sirenltd.dev/hvac"
    title = "HVAC - HomeBuddy"
    button_homepage = "button[data-autotest-button-button-go-to-homepage='']"
    text_sorry = "//h3[contains(text(),'Sorry to see you go!')]"
    text_check_out = "//div[contains(text(),'Check out the other services that we offer.')]"
