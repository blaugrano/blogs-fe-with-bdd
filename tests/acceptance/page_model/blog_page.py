from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):

    @property
    def url(self):
        return super().url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POSTS)
