from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class PostPageLocators(BasePageLocators):
    POST_FORM = By.ID, 'post-form'
    TITLE_FIELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'
