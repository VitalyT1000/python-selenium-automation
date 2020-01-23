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

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_button = driver.find_element(By.XPATH, "//div[@id='nav-search']//input[@value='Go'][@class='nav-input']")
search.clear()
search.send_keys('Lego')

search_button.click()
search.clear()

# verify
assert 'Lego' in driver.find_element(By.XPATH, "//div[@id='search']//div[@class='______']//span[@class='a-color-state a-text-bold']").text

driver.quit()

