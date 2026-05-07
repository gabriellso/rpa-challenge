from selenium.webdriver.common.by import By

import time


FIELD_MAPPING = {
    "First Name": "labelFirstName",
    "Last Name": "labelLastName",
    "Company Name": "labelCompanyName",
    "Role in Company": "labelRole",
    "Address": "labelAddress",
    "Email": "labelEmail",
    "Phone Number": "labelPhone"
}


def fill_form(driver, data):

    for field_name, value in data.items():

        if field_name not in FIELD_MAPPING:
            continue

        reflect_name = FIELD_MAPPING[field_name]

        input_element = driver.find_element(
            By.XPATH,
            f"//input[@ng-reflect-name='{reflect_name}']"
        )

        input_element.clear()

        input_element.send_keys(str(value))

        time.sleep(0.05)