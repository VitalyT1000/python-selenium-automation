from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=r'./drivers/chromedriver')

# init driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

# open the url
driver.get('https://www.amazon.com/')
sleep(1)

driver.get('https://www.amazon.com/gp/help/customer/display.html')
sleep(1)

search = driver.find_element(By.XPATH, "//input[@type='search']")
search.send_keys('Cancel order')
sleep(1)
search_button = driver.find_element(By.XPATH, "//input[@class='a-button-input']")
search_button.click()


# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']").text


sleep(1)
driver.quit()