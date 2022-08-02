from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class HomePageLocators(BasePageLocators):
    NAVIGATION_LINK = By.ID, 'blog-link'
