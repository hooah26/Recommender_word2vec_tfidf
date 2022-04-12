from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen


from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException



option = webdriver.ChromeOptions()
#options.add_argument('headless')
option.add_argument('lang=ko_KR')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
option.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=option)
driver.implicitly_wait(10)


coupang_url = 'https://www.coupang.com/vp/products/6226601387?itemId=12490847528&vendorItemId=74407923474&q=%EC%A0%9C%EB%A1%9C+%EC%BD%9C%EB%9D%BC&itemsCount=36&searchId=3b16719735cd4b74833bdf2f5e05a192&rank=0&isAddedCart='
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
driver.get(coupang_url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, 700)")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="btfTab"]/ul[1]/li[2]').click()
time.sleep(2)


reviews= []
for j in range (2, 13):
	try:
		driver.find_element_by_xpath(f'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button[{j}]').click()
		time.sleep(1)
	except:
		print('page_error')

	for i in range (1, 6):
		try:
			review = driver.find_element_by_xpath(f'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/article[{i}]/div[4]/div').text
			review = re.sub('[^가-힣 ]', ' ', review)
			reviews.append(review)
		except:
			print('review_error')

for i in range (3, 12):
	try:
		driver.find_element_by_xpath(f'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/div[3]/button[{j}]').click()
		time.sleep(1)
	except:
		print('page_error')

	for i in range (1, 6):
		try:
			review = driver.find_element_by_xpath(f'//*[@id="btfTab"]/ul[2]/li[2]/div/div[6]/section[4]/article[{i}]/div[4]/div').text
			review = re.sub('[^가-힣 ]', ' ', review)
			reviews.append(review)
		except:
			print('review_error')

print(len(reviews))
