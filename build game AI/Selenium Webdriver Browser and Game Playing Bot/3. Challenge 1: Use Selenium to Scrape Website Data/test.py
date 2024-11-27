from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get('https://time.is/vi/')

while 1<2:
    time_now = driver.find_element(By.XPATH, value='//*[@id="clock0_bg"]')
    print('got time element')
    print(time_now.text)
    time.sleep(5)
    driver.refresh()
    print('\nrefreshed')


# Update in real-time (does display on webpage live - FRONT-END).
# Update in real-time (BUT does NOT display on webpage live - BACK-END/SERVER - JS?).
