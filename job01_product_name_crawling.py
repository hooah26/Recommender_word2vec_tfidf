from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}

product_names=[]
for i in range(1, 18):
    try:
        url = 'https://www.coupang.com/np/categories/195050?channel=plp_C2&page={}'.format(i)
        # print(url)
        res = requests.get(url, headers=headers, timeout=10)
        html = res.content.decode('utf-8', 'replace')
        res.raise_for_status()
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find("ul",{"id":"productList"})
        try:
            product_names += ([p.text for p in contents.find_all("div",{"class":"name"})])
            print(product_names)
            time.sleep(1)
        except:
            print('product_name_error')
            continue

    except:
        print('page_error')
        continue

df = pd.DataFrame({'product_name':product_names})
df.to_csv('./crawling_data/product_name.csv', encoding='utf-8-sig', index=False)
print(len(product_names))
