from selenium.webdriver.common.by import By

from tests.acceptance.locators.home_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def links(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)