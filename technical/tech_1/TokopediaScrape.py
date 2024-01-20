import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def tokpedscrape (keyword, page):
    driver = webdriver.Firefox()
    url = (f"https://www.tokopedia.com/search?st=&q={keyword}&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=")
    driver.get(url)
    counter_page = 0
    datas = []

    while counter_page < page:
        try:
            for _ in range(0, 7500, 500):
                time.sleep(0.1)
                driver.execute_script("window.scrollBy(0,500)")

            card = driver.find_elements(By.XPATH, "//div[@class='css-llwpbs']")

            for i in range(len(card)):
                try:
                    sold_element = card[i].find_element(By.XPATH, ".//div/div/div/div/div/div[2]/a//span[@class='prd_label-integrity css-1sgek4h']").text
                except NoSuchElementException:
                    sold_element = "0"

                try:
                    name_element = card[i].find_element(By.XPATH, ".//div/div/div/div/div/div[2]/a/div[@data-testid='spnSRPProdName']").text
                except NoSuchElementException:
                    name_element = card[i].find_element(By.XPATH, ".//div/div/div/div/div/div[2]/a/div[@class='prd_link-product-name css-3um8ox']").text
                
                try:
                    price_element = card[i].find_element(By.XPATH, ".//div/div/div/div/div/div[2]/a//div[@class='prd_link-product-price css-h66vau']").text,
                except NoSuchElementException:
                    price_element = "no price listed"

                datas.append({
                    'name': name_element,
                    'price': price_element,
                    'sold': sold_element,
                    'page': counter_page+1
                })

            counter_page += 1

            next_page = driver.find_element(By.XPATH, "//button[@aria-label='Laman berikutnya']")
            if next_page.is_enabled():
                next_page.click()
            else:
                print("result page limit reached, exiting")
                counter_page = page

        except Exception as e:
            print("ERROR", e)
            break
    df = pd.DataFrame(datas)
    driver.close()
    preprocess(df,keyword,page)
    
def preprocess (df,keyword,page):
    df['name'] = df['name'].astype(str)
    df['name'] = df['name'].str.replace('"', '')

    df['price'] = df['price'].astype(str)

    # Add an if check to perform split or extract based on the presence of "-"
    df['price'] = df['price'].apply(lambda x: x.split(' - ') if '-' in x else [x])

    # chatgpt helped to build the lambda function and combine them in one line
    df['price'] = df['price'].apply(lambda x: [(value.replace("Rp", "").replace("jt", "00000").replace(",", "").replace(".", "").replace('"', "").replace(")", "").replace("(", "").replace("'", "").replace("rb", "000")) for value in x])

    df['price'] = df['price'].apply(lambda x: [int(value) for value in x])

    # get average between two prices
    df['price'] = df['price'].apply(lambda x: round(sum(x)/len(x)))

    df['sold'] = df['sold'].astype(str)
    df['sold'] = df['sold'].str.replace('terjual', '',regex=True).str.replace('rb', '000',regex=True).str.replace('+', '',regex=True).astype(int)
    df['sold'] = df['sold'].astype(int)

    df['gmv'] = df['price'] * df['sold']

    df.to_csv(f'{keyword}_{page}.csv', index=False)
    print(f"scraping for {keyword} with {page} pages done")
    return df

def __main__():
    # tokpedscrape("xiaomi", 3)
    tokpedscrape("Rockbros", 1)
    tokpedscrape("Matoa",5)
    tokpedscrape("konichiwa", 10)

__main__()