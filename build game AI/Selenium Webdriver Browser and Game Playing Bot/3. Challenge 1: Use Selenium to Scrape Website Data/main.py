from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(options=firefox_options)

driver.get("https://www.python.org/")

# solution 1:
# time_python_org_1 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# # print(time_python_org_1.text)
# name_python_org_1 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# # print(time_python_org_1.text)
#
# time_python_org_2 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time')
# name_python_org_2 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a')
# # print(time_python_org_2.text)
#
# time_python_org_3 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/time')
# name_python_org_3 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a')
# # print(time_python_org_3.text)
#
# time_python_org_4 = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/time')
# name_python_org_4 = driver.find_elem

# solution 2:
# list = []
#
# for i in range(1, 6):
#     list.append(
#         {
#     "time":driver.find_element(By.XPATH, value= f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text,
#     "name":driver.find_element(By.XPATH, value= f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
#         }
#     )
# print(list)

# solution 3:
# import pprint
# time_list = [item.text for item in (driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').find_elements(By.TAG_NAME, value = "time"))]
# date_list = [item.text for item in (driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').find_elements(By.TAG_NAME, value = "a"))]
# final_list = []
# if len(time_list) == len(date_list):
#     for i in range(0, len(time_list)):
#         final_list.append(
#             {
#         "time":time_list[i],
#         "name":date_list[i]
#             }
#         )
# else:
#     print(len(time_list))
#     print(len(date_list))
# pprint.pp(final_list)
# driver.quit()