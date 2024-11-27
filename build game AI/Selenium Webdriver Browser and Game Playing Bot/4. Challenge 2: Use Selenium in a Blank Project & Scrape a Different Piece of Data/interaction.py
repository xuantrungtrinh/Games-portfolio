from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# articles_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(articles_number.text)
# articles_number.click()

# FIND ELEMENT BY LINK TEXT:
# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# FIND THE "SEARCH" <INPUT> BY NAME:
search = driver.find_element(By.NAME, value='search')

# SENDING KEYBOARD INPUT TO SELENIUM:
search.send_keys("Python", Keys.ENTER)
# driver.close() #closes a SINGLE TAB -
