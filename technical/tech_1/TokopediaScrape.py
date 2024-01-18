import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
url = "https://www.tokopedia.com/search?st=&q=rockbros&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver.get(url)

counter_page = 0
datas = []

while counter_page < 2:
    try:
        for _ in range(0, 7500, 500):
            time.sleep(0.1)
            driver.execute_script("window.scrollBy(0,500)")


        # count number of figure tags

        # title = driver.find_elements(
        #     By.XPATH, "//div[@class='prd_link-product-name css-3um8ox']")
        # price = driver.find_elements(
        #     By.XPATH, "//div[@class='prd_link-product-price css-h66vau']")
        # sold = driver.find_elements(
        #     By.XPATH, "//span[@class='prd_label-integrity css-1sgek4h']")
        # print(len(card))
        # print(len(title))
        # print(len(price))
        # print(len(sold))

        # for i in range(len(title)):
        #     datas.append({
        #         'name': title[i].text,
        #         'price': price[i].text,
        #         'sold': sold[i].text
        #     })

        card = driver.find_elements(
            By.XPATH, "//div[@class='css-llwpbs']")

        for i in range(len(card)):
            datas.append({
                'name': card[i].find_element(By.XPATH, ".//div/div/div/div/div/div[2]/a/div[@class='prd_link-product-name css-3um8ox']").text,
            })

        counter_page += 1
        next_page = driver.find_element(
            By.XPATH, "//button[@aria-label='Laman berikutnya']")
        next_page.click()
    except Exception as e:
        print("ERROR", e)
        break

# convert datas into dataframe
df = pd.DataFrame(datas)
# export dataframe to csv
df.to_csv('tokopedia.csv', index=False)
