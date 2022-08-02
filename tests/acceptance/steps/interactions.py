from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@when('I click on "(.*)" link')
def step_impl(context, link_text):
    links = BasePage(context.driver).links
    links = [x for x in links if x.get_attribute('text') == link_text]

    if len(links) > 1:
        raise RuntimeError(f'Page contains more than 1 link with {link_text} text')
    else:
        links[0].click()


@when('I enter "(.*)" in the field "(.*)"')
def step_impl(context, content, name):
    page = PostPage(context.driver)
    page.form_field(name).send_keys(content)

@when('I press the submit button')
def step_impl(context):
    PostPage(context.driver).submit_button.click()
