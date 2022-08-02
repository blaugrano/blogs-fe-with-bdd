from selenium.webdriver.chrome.options import Options
from behave import *
from selenium import webdriver

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@given("I am on the home page")
def step_impl(context):
    context.driver = webdriver.Chrome('/usr/bin/chromedriver')
    context.driver.get(HomePage(context.driver).url)


@given("I am on the blog page")
def step_impl(context):
    chrome_options = Options()
    context.driver = webdriver.Chrome('/usr/bin/chromedriver')
    context.driver.set_page_load_timeout(5)
    context.driver.implicitly_wait(5)
    context.driver.get(BlogPage(context.driver).url)

@given("I am on the new post page")
def step_impl(context):
    context.driver = webdriver.Chrome('/usr/bin/chromedriver')
    context.driver.get(PostPage(context.driver).url)


@then("I am on the blog page")
def step_impl(context):
    assert context.driver.current_url == BlogPage(context.driver).url
