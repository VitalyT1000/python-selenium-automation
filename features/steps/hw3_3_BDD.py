from time import sleep
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

CART_BUTTON = (By.ID, 'nav-cart')
CART_CHECK = (By.CSS_SELECTOR, ".sc-empty-cart-header")

# @given('Open Amazon web-site')
# def open_amazon_page(context):
#     context.driver.get('https://www.amazon.com/')
#     sleep(2)

@when('Click Cart icon')
def click_cart_button(context):
    amazon_cart_button = context.driver.find_element(*CART_BUTTON)
    amazon_cart_button.click()
    sleep(2)

@then('Check the Cart have to be empty')
def check_amazon_cart(context):
    assert 'Cart is empty' in context.driver.find_element(*CART_CHECK).text