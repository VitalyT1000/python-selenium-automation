from time import sleep
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# # init driver
# driver = webdriver.Chrome()
# # driver = webdriver.Chrome(executable_path=r'./drivers/chromedriver')
#
# # init driver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(chrome_options=chrome_options)

SEARCH_INPUT_LOCATOR = (By.ID, 'helpsearch')
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@class='a-button-input']")
HEADER_PAGE_LOCATOR = (By.CSS_SELECTOR, ".help-content h1")

# open the url
@given('Open Amazon web-site')
#driver.get('https://www.amazon.com/')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)

@given('Click Help button')
#driver.get('https://www.amazon.com/gp/help/customer/display.html')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    sleep(2)

@when('Input Cancel order into Find more solution field')
# search = driver.find_element(By.XPATH, "//input[@type='search']")
# search.clear()
# search.send_keys('Cancel order')
def search_input_fill(context):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys('Cancel order')
    sleep(2)

@when('Click GO button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(2)


# search_button = driver.find_element()
# search_button.click()


# verify
@then('Result contains Cancel Items or Orders')
def check_header_page(context):
    assert 'Cancel Items or Orders' in context.driver.find_element(*HEADER_PAGE_LOCATOR).text


    sleep(2)
#driver.quit()