from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.co.uk/Instant-Electric-Pressure-Cooker-Programmes/dp/B082VBDR94")
driver.get("https://translate.google.com/translate?hl=vi&sl=en&u=https://www.amazon.com/&prev=search&pto=aue")

price_dollar = driver.find_element(By.CLASS_NAME, value="priceToPay")
# price_cents = driver.find_element(By.CLASS_NAME)
#
print(f'The price is {price_dollar.text}')

driver.close() #closes a SINGLE TAB -

# DE DO NHUC DAU VA DO MAT THOI GIAN, MINH SE DUNG EDGE (VI VAN DE HIEN TAI LA AMAZON NO DUNG CAPTCHA)!