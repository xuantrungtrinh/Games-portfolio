from selenium import webdriver
from selenium.webdriver.common.by import By
import time

safari_options = webdriver.SafariOptions()

driver = webdriver.Safari(options=safari_options)

# driver.get("https://www.amazon.com/Sweatshirts-Leggings-Gaharu-Flannel-Checkered/dp/B09LLR57F3/ref=s9_acsd_al_ot_c2_x_1_t?_encoding=UTF8&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=4RSH8JD5A17Y1WQ64MD9&pf_rd_p=10417c57-9940-4eb9-8120-5966969c4f81&pf_rd_t=&pf_rd_i=19277531011&th=1")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver.get("https://www.python.org/")


# price_dollar = driver.find_element(By.CLASS_NAME, value="priceToPay")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price").find_element(By.CLASS_NAME, value="a-price-fraction")
# price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# print(f'The price is {price_dollar.text}{price_cents.text} ({price_symbol.text})')

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a") # find any anchor tags. And to express that as a CSS selector we would specify the class, documentation-widget. And then inside the element with that class, we're looking for an anchor tag.
# print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_attribute(name="href"))

# driver.close() #closes a SINGLE TAB
driver.quit()


# Keep the browser open indefinitely
# while 1<2:
#     try:
#         # if ...:
#         #
#         # else:
#         #     time.sleep()
#         time.sleep(1)
#
#
#
#
#     except KeyboardInterrupt:
#         print("Closing browser...")
#         driver.quit()
#     