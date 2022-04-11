from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


df = pd.read_csv('./crawling_data/reviews_1020.csv')
stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_names = []
for name in df.drink_name:
    name = re.sub('[^가-힣 ]', '', name)
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
df.drop_duplicates(inplace=True)
df.to_csv('./crawling_data/cleaned_names.csv', index=False)
df.info()