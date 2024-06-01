import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given("Init webdriver chrome")
def before_all(context):
    context.browser = webdriver.Chrome()


@when("we implement a test")
def step_impl(context):
    context.browser.get("http://localhost:8000")
    print("title " + context.browser.title)
    assert "To-Do" in context.browser.title
    header_text = context.browser.find_element(By.TAG_NAME, "h1").text
    assert "To-Do" in header_text

    inputbox = context.browser.find_element(By.ID, "id_new_item")
    assert inputbox.get_attribute("placeholder") == "Enter a to-do item"

    inputbox.send_keys("Buy peacock feathers")
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = context.browser.find_element(By.ID, "id_list_table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    assert any(row.text == "1: Buy peacock feathers" for row in rows)

    assert False, "Finish the test!"


def after_all(context):
    context.browser.quit()
