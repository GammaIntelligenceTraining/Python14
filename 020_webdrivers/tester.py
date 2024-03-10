from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.gammatest.net')

# driver.find_element('link text', 'Подробнее').click()

gamma = driver.current_window_handle

driver.switch_to.new_window('tab')
driver.get('http://www.github.com')

github = driver.current_window_handle

time.sleep(2)
driver.switch_to.window(gamma)

print(driver.window_handles)

time.sleep(3)