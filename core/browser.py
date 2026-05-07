from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def start_browser():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(),
        options=options
    )

    return driver