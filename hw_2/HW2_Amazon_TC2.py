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

search_button = driver.find_element(By.XPATH, "//span[@class='nav-line-2'][text()='& Orders']")
search_button.click()

# verify
assert 'Sign-In' in driver.find_element(By.XPATH, "//div[@class='a-section']//h1[@class='a-spacing-small']").text

sleep(1)
driver.quit()