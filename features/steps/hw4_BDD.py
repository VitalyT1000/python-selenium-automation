from time import sleep
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

COMMAND_LINE = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.XPATH, "//input[@type='submit'][@class='nav-input']")
FIRST_ITEM = (By.XPATH, "//div[@id='anonCarousel1']//li[@aria-posinset='2']")
ADD_CART = (By.ID, 'add-to-cart-button')
CART_CHECK = (By.ID, 'sc-subtotal-label-activecart')

# @given('Open Amazon web-site') - existing step
# def open_amazon_page(context):
#     context.driver.get('https://www.amazon.com/')
#     sleep(2)

@when('Search input fill Toys')
def search_input_toys(context):
    input_toys = context.driver.find_element(*COMMAND_LINE)
    input_toys.clear()
    input_toys.send_keys("Toys")

@when('Click search button')
def amazon_search_button(context):
    search_button = context.driver.find_element(*SEARCH_BUTTON)
    search_button.click()
    sleep(2)

@when('Choose the first Item')
def choose_first_item(context):
    first_item = context.driver.find_element(*FIRST_ITEM)
    first_item.click()
    sleep(1)

@when('Add Toys to the Cart')
def add_item_cart(context):
    add_item = context.driver.find_element(*ADD_CART)
    add_item.click()
    sleep(1)

#@when('Click Cart icon') - existing step

@then('Check the Cart is NOT empty')
def amazon_cart_check(context):
    assert 'Subtotal' in context.driver.find_element(*CART_CHECK).text



