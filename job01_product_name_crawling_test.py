from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
import urllib


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}

imgs=[]
hrefs=[]
names=['박카스','콜라','사이다']
for name in names :
    url = 'https://www.coupang.com/np/search?component=&q={}&channel=user'.format(name)
    res = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(res.text,'html.parser')
    img = soup.find("img",{"class":"search-product-wrap-img"})['src']
    href = soup.find('a',{'class':'search-product-link'})['href']
    product_name = soup.find('div',{'class':'name'}).get_text()
    URL = 'https:' + img
    href_URL = 'https://www.coupang.com/' + href
    imgs.append(URL)
    hrefs.append(href_URL)
    # # img = urllib.request.urlopen(URL).read()
print(hrefs)




# print(len(hrefs))
#