import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/crawling_data.csv')
print(df.head())
df.info()
#
# for i in range(len(df)):
#     if len(df.iloc[i, 1]) > 1000:
#         df.iloc[i, 1] = df.iloc[i, 1][:1000]

stopwords = pd.read_csv('./crawling_data/stopwords.csv')
stopwords_list = list(stopwords['stopword'])
cleaned_sentences = []
for review in df.reviews:
    review = re.sub('[^가-힣 ]', '', review)
    review_word = review.split(' ')



    words = []
    for word in review_word:
        if len(word) > 1:
            if word not in stopwords_list:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_sentences'] = cleaned_sentences
df = df[['product', 'cleaned_sentences']]
df=df.drop_duplicates(['cleaned_sentences'], keep='first')
df.to_csv('./crawling_data/cleaned_data.csv',
          index=False)
df.info()