from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
last_name = driver.find_element(By.XPATH, value= '/html/body/form/input[2]')
email_address = driver.find_element(By.XPATH, value= '/html/body/form/input[3]')
sign_up_button = driver.find_element(By.XPATH, value= '/html/body/form/button')

first_name.send_keys('Tr Lee Ho')
last_name.send_keys('Min')
email_address.send_keys('abcxyz@email.com', Keys.ENTER)
# or:
# sign_up_button.click()

# driver.quit()