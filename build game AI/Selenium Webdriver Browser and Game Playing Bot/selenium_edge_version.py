from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_dollar = driver.find_element(By.CLASS_NAME, value="priceToPay")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f'The price is {price_dollar.text}.{price_cents}')

driver.close() #closes a SINGLE TAB -