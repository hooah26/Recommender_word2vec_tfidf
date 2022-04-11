from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}

raw_productLists=[]
for i in range(1, 18):
    url = 'https://www.coupang.com/np/categories/195050?channel=plp_C2&page={}'.format(i)
    # print(url)
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8', 'replace')
    res.raise_for_status()
    soup = BeautifulSoup(html, 'html.parser')
    contents = soup.find("ul",{"id":"productList"})
    raw_productLists += ([p.text for p in contents.find_all("div",{"class":"name"})])
    print(raw_productLists)

df = pd.DataFrame({'drink_name':raw_productLists})
df.to_csv('./reviews_{}.csv'.format(len(df)), encoding='utf-8-sig', index=False)
# print(len(raw_productLists))

stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_names = []
for name in df.drink_name:
    name = re.sub('[^가-힣 ]', '', v)
    new_name = name.split(' ')

    new_names = []
    for name in new_name:
        if len(name) > 1:
            if name not in stopwords_list:
                new_names.append(name)
    cleaned_name = ' '.join(new_names)
    cleaned_names.append(cleaned_name)
df['cleaned_names'] = cleaned_names
df = df[['cleaned_names']]
df.to_csv('./crawling_data/cleaned_names.csv', index=False)
df.info()