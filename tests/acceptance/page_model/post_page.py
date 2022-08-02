from selenium.webdriver.common.by import By
from tests.acceptance.locators.post_page import PostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class PostPage(BasePage):

    @property
    def url(self):
        return super().url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*PostPageLocators.POST_FORM)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

    @property
    def submit_button(self):
        return self.driver.find_element(*PostPageLocators.SUBMIT_BUTTON)
