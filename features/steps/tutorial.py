from behave import *
from selenium import webdriver


@given("Init webdriver chrome")
def before_all(context):
    context.browser = webdriver.Chrome()


@when("we implement a test")
def step_impl(context):
    assert context.browser.title is "To-Do"


def after_all(context):
    context.browser.quit()
