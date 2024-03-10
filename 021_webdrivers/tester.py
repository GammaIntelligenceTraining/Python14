from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('http://www.google.com')

reject = driver.find_element('id', 'W0wltc')
reject.click()

# search = driver.find_element('xpath', '//*[@id="APjFqb"]')
# search.send_keys('Selenium documentation')
# time.sleep(2)
# search.clear()

# print(search.is_enabled())
# print(search.is_selected())
# print(search.is_displayed())

# search.send_keys(Keys.RETURN)
# driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
# time.sleep(5)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(2)

# width = driver.get_window_size()['width']
# height = driver.get_window_size().get('height')
# print(driver.get_window_size())
#
# driver.set_window_size(1920, 1080)
#
# print(driver.get_window_position())
# driver.set_window_position(0, 0)
#
# print(driver.get_window_rect())
# driver.set_window_rect(100, 100, 400, 900)

# driver.fullscreen_window()
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# driver.minimize_window()

# driver.save_screenshot('img.png')
#
# el = driver.find_element('css selector', 'body > div.L3eUgb > div.o3j99.n1xJcf.Ne6nSd')
# el.screenshot('element.png')

google = driver.current_window_handle
driver.switch_to.new_window('tab')
driver.get('http://www.github.com')
github = driver.current_window_handle
time.sleep(2)
driver.switch_to.window(google)
print(driver.window_handles)
# time.sleep(2)
# driver.close()
print(driver.page_source.encode())

time.sleep(3)
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("http://www.google.com")
# def waiter(timeout, selector, value):
#     try:
#         element = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located((selector, value))
#         )
#     except:
#         print('ERROR')
#         return None
#     else:
#         return element
#
# reject = waiter(10, By.ID, 'W0wltc')
# print(reject)

