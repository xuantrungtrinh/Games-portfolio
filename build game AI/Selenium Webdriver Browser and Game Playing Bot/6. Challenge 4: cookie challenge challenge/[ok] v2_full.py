from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.SafariOptions()
# options.add_experimental_option("detach", True)

driver=webdriver.Safari(options=options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

def buy_item(string_item_name):
    while 1 < 2:
        try:
            while 1 < 2:
                try:
                    money = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#money")))
                    break
                except Exception as e:
                    print(f'{e} - FIXED THOUGH')
                    pass
            money_text = money.text
            if ',' in str(money.text):
                money_text = str(money.text).replace(',', '')
            print(f'money now is {money_text}')
            while 1 < 2:
                try:
                    item_name = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#buy{string_item_name} b")))
                    break
                except Exception as e:
                    print(f'{e} - FIXED THOUGH')
                    pass
            item_cost = item_name.text.split('-')[1].strip()
            if ',' in str(item_name.text.split('-')[1].strip()):
                item_cost = str(item_name.text.split('-')[1].strip()).replace(',', '')
            if int(money_text) >= int(item_cost):
                while 1 < 2:
                    try:
                        item_name = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#buy{string_item_name} b")))
                        item_name.click()
                        break
                    except Exception as e:
                        print(f'{e} - FIXED THOUGH')
                        pass
                print(f"bought new {string_item_name}!")
            else:
                print(f'cant buy {string_item_name}')
                break
        except Exception as e:
            print("error try -- REFRESHED TO GET ALL NEEDED THINGS AGAIN, AND TRIED TO CLICK AGAIN - DONT WORRY!!")
            print(e)
            pass

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

Cursor = "Cursor"
Grandma = "Grandma"
Factory = "Factory"
Mine = "Mine"
Shipment = "Shipment"
Alchemy_lab = "Alchemy\\ lab"
Portal = "Portal"
Time_machine = "Time\\ machine"

now = time.time()

while 1<2:
    cookie.click()
    if (round(time.time()) - now) >= 5:
        buy_item(Time_machine)
        buy_item(Portal)
        buy_item(Alchemy_lab)
        buy_item(Shipment)
        buy_item(Mine)
        buy_item(Factory)
        buy_item(Grandma)
        buy_item(Cursor)
        # reset counting down time:
        now = time.time()
        print(f"time now is: {now}")
    else:
        print("not")

# item_name = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#buyTime\\ machine b")))
# print(item_name.text)