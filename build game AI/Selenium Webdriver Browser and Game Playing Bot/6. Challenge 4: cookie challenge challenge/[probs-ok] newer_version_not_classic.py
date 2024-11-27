from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver=webdriver.Edge(options=options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

def buy_item(number_item_name):
    letters_in_name = {"million":"000000", "billion":"000000000",
                       "trillion": "000000000000", "quadrillion":"000000000000000",
                       "quintillion":"000000000000000000", "sextillion":"000000000000000000000",
                       "septillion":"000000000000000000000000", "octillion": "000000000000000000000000",
                       "nonillion":"000000000000000000000000000", "decillion":"000000000000000000000000000000"}
    while 1 < 2:
        try:
            while 1 < 2:
                try:
                    money = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cookies")))
                    break
                except Exception as e:
                    print(f'{e} - FIXED THOUGH')
                    pass
            money_text = money.text

            if ' ' in str(money.text):
                money_text = str(money_text).split(' ')[0].strip()
            if ',' in str(money.text):
                money_text = str(money_text).replace(',', '')
            if '.' in str(money.text):
                money_text = str(money_text).replace('.', '')
            for letter in letters_in_name:
                if str(letter) in money.text:
                    money_text = money_text + letters_in_name[letter]

            print(f'money now is {money_text}')
            while 1 < 2:
                try:
                    # item_name = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#productName{number_item_name}")))
                    # item_price = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#productPrice{number_item_name}")))
                    item_price_raw = driver.find_element(By.CSS_SELECTOR, f"#productPrice{number_item_name}")
                    print(f"got item PRICE: {item_price_raw.text}")
                    break
                except Exception as e:
                    print(f'{e} - FIXED THOUGH')
                    pass
            item_price = item_price_raw.text

            if ' ' in str(item_price_raw.text):
                item_price = str(item_price).split(' ')[0].strip()
            if ',' in str(item_price_raw.text):
                item_price = str(item_price).replace(',', '')
            if '.' in str(item_price_raw.text):
                item_price = str(item_price).replace('.', '')
            for letter in letters_in_name:
                if str(letter) in item_price_raw.text:
                    item_price = item_price + letters_in_name[letter]
            if item_price_raw.text == '':
                break
            print(f'money is now: {money_text}\nitem_price is now {item_price}')
            if int(money_text) >= int(item_price):
                while 1 < 2:
                    try:
                        item = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#product{number_item_name}")))
                        item.click()
                        break
                    except Exception as e:
                        print(f'{e} - FIXED THOUGH')
                        pass
                print(f"bought new {number_item_name}!")
            else:
                print(f'cant buy {number_item_name}')
                break
        except Exception as e:
            print("error try -- REFRESHED TO GET ALL NEEDED THINGS AGAIN, AND TRIED TO CLICK AGAIN - DONT WORRY!!")
            print(e)
            pass

# cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))


now = time.time()

choose_language_on_startup = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]')))
choose_language_on_startup.click()
time.sleep(4)

while 1<2:
    cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bigCookie')))
    # cookie = driver.find_element(By.TAG_NAME, value='button').find_element(By.CSS_SELECTOR, value='#bigCookie')

    cookie.click()
    print("clicked cookie")

    if (round(time.time()) - now) >= 30:
        for i in range(19, -1, -1):
            i_str = str(i)
            buy_item(i_str)
            # reset counting down time:
        now = time.time()
        print(f"time now is: {now}")
    else:
        print("not")



