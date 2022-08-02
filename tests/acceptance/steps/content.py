from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then("There is a title shown on the page")
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The tile tag has content "(.*)"')
def step_impl(context, content):
    assert BasePage(context.driver).title.text == content


@then("I can see a posts section on the page")
def step_impl(context):
    assert BlogPage(context.driver).posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    posts = BlogPage(context.driver).posts
    posts_with_title = [post for post in posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])
