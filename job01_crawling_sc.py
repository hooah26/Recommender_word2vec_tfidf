from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
url = 'https://www.coupang.com/np/categories/195050?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194950&rating=0'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
contents = soup.find_all("li",{"class":"baby-product renew-badge"})


product_list = []
for content in contents:
    # try:
    data_product_id = content.find('a')['data-product-id']
    data_item_id = content.find('a')['data-item-id']
    data_vendor_item_id = content.find('a')['data-vendor-item-id']
    url1 = 'https://www.coupang.com/vp/products/{}?itemId={}&vendorItemId={}&sourceType=CATEGORY&categoryId=194950&isAddedCart='.format(data_product_id,data_item_id,data_vendor_item_id)
    print('debug01')
    try:
        res = requests.get(url1, headers=headers, timeout=1)
    except:
        print('error')
        continue
    print('debug02')
    soup = BeautifulSoup(res.text, 'html.parser')
    print('debug03')
    product = soup.find("h2", {"class": "prod-buy-header__title"})
    print(product)
    product_list.append(product.get_text())
    # except:
    #     continue
print(product_list)

