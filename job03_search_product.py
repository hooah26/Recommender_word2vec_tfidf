from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

option = webdriver.ChromeOptions()
option.add_argument('lang=ko_KR')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
option.add_argument('disable-gpu')

df = pd.read_csv('./crawling_data/cleaned_product_name.csv')
product_names = list(df.product_name)
print(product_names)


for product_name in product_names:

    driver = webdriver.Chrome('./chromedriver', options=option)
    driver.implicitly_wait(10)
    print(product_name)

    coupang_url = 'https://www.coupang.com/np/categories/194276'
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })

    driver.get(coupang_url)
    time.sleep(1)

    element = driver.find_element_by_name('q')
    element.send_keys(product_name)
    element.submit()
    time.sleep(1.5)


    ele = driver.find_elements_by_class_name('no-1')
    ele[0].click()

    time.sleep(2)

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after) # 새로운 창 hand하기

    driver.execute_script("window.scrollTo(0, 700)")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="btfTab"]/ul[1]/li[2]').click()
    time.sleep(1.5)

    reviews = []
    for h in range(1, 3):
        time.sleep(1)
        f = False
        for j in range(2, 12):

            if f == False:
                try:
                    # d = False
                    driver.find_element_by_xpath(f'/html/body/div[2]/section/div[2]/div[10]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button[{j}]').click()
                    time.sleep(1)
                    print(h,'쪽',j,'페이지')

                    for i in range(1, 6):
                        try:
                            review = driver.find_element_by_xpath(
                                f'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/article[{i}]/div[4]/div').text
                            review = re.sub('[^가-힣 ]', ' ', review)
                            reviews.append(review)
                            print(h, '쪽', j, '페이지', i, '번째')
                        except:
                            print('review_error')
                            f = True
                            break

                except:
                    print('page_error')
                    break
            else:
                break
        try:
            driver.find_element_by_xpath('//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button[12]').click()
            time.sleep(1)
        except:
             print('페이지없음')
             break
    print(len(reviews))

    df = pd.DataFrame({'reviews': reviews})
    # print(df.tail())
    df.to_csv('./review_data/reviews_{}.csv'.format(product_name), index=False)
    driver.quit()

