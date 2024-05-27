from behave import *
from selenium import webdriver


@given("Init webdriver chrome")
def before_all(context):
    context.browser = webdriver.Chrome()


@when("we implement a test")
def step_impl(context):
    print("title " + context.browser.title)
    assert "To-Do" in context.browser.title


def after_all(context):
    context.browser.quit()
