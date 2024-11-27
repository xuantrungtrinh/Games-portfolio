from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
# options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
# safari_options = webdriver.SafariOptions()
# firefox_options = webdriver.FirefoxOptions() # Firefox cham VCL.

driver=webdriver.Chrome(options=options)
# driver = webdriver.Edge(options=options)
# driver = webdriver.Safari(options=safari_options)
# driver = webdriver.Firefox(options=firefox_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

# USING XPATH:
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
# Cursor = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]')
# Grandma = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
Factory = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]')
Mine = driver.find_element(By.XPATH, value='//*[@id="buyMine"]')
Shipment = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]')
Alchemy_lab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
Portal = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]')
Time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')

# money = driver.find_element(By.CSS_SELECTOR, value='#money')

# USING ... ==> get a list of those items:
# ...

now = time.time()

while 1<2:
    cookie.click()
    if round(time.time()) - now >= 5:
        # while 1<2:
        #     try:
        #         Time_machine.click()
        #     except:
        #         print('cant buy')
        #         break
        # while 1 < 2:
        #     try:
        #         Portal.click()
        #     except:
        #         print('cant buy')
        #         break
        # while 1 < 2:
        #     try:
        #         Alchemy_lab.click()
        #     except:
        #         print('cant buy')
        #         break
        # while 1 < 2:
        #     try:
        #         Shipment.click()
        #     except:
        #         print('cant buy')
        #         break
        # while 1 < 2:
        #     try:
        #         Mine.click()
        #     except:
        #         print('cant buy')
        #         break
        # while 1 < 2:
        #     try:
        #         Factory.click()
        #     except:
        #         print('cant buy')
        #         break
        while 1 < 2:
            try:
                # money = driver.find_element(By.CSS_SELECTOR, value='#money')
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
                # Grandma = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
                while 1<2:
                    try:
                        Grandma = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyGrandma b")))
                        break
                    except Exception as e:
                        print(f'{e} - FIXED THOUGH')
                        pass
                Grandma_cost = Grandma.text.split('-')[1].strip()
                if ',' in str(Grandma.text.split('-')[1].strip()):
                    Grandma_cost = str(Grandma.text.split('-')[1].strip()).replace(',', '')
                if int(money_text) >= int(Grandma_cost):
                    Grandma.click()
                    print("bought new grandma!")
                else:
                    print('cant buy Grandma')
                    break
            except Exception as e:
                print("error try -- REFRESHED TO GET ALL NEEDED THINGS AGAIN, AND TRIED TO CLICK AGAIN - DONT WORRY!!")
                print(e)
                pass
        while 1 < 2:
            try:
                # money = driver.find_element(By.CSS_SELECTOR, value='#money')
                while 1<2:
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
                # Cursor = driver.find_element(By.CSS_SELECTOR, value='#buyCursor b')
                while 1<2:
                    try:
                        Cursor = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyCursor b")))
                        break
                    except Exception as e:
                        print(f'{e} - FIXED THOUGH')
                        pass
                Cursor_cost = Cursor.text.split('-')[1].strip()
                if ',' in str(Cursor.text.split('-')[1].strip()):
                    Cursor_cost = str(Cursor.text.split('-')[1].strip()).replace(',', '')
                if int(money_text) >= int(Cursor_cost):
                    Cursor.click()
                    print("bought new cursor!")
                else:
                    print('cant buy Cursor')
                    break
            except Exception as e:
                print("error try -- REFRESHED TO GET ALL NEEDED THINGS AGAIN, AND TRIED TO CLICK AGAIN - DONT WORRY!!")
                print(e)
                pass
        now = time.time()
        print(f"time now is: {now}")

    # if round(time.time()) - now >= 20:
    #     want_to_continue = False
    #     while want_to_continue == False:
    #         ask = input("Do you like to continue??")
    #         if ask.lower() == "yes":
    #             want_to_continue
    #             = True
    #             now = time.time()
    #         elif ask.lower() == "no":
    #             driver.quit()
    #         else:
    #             print("input re-input 'yes' or 'no'\n")