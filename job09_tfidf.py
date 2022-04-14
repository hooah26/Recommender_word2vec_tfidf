import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./crawling_data/drink_onesentence.csv')
df_reviews.dropna(inplace=True)
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_reviews['cleaned_sentences'])

with open('./models/drink.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)
mmwrite('./models/drink.mtx', Tfidf_matrix)
print('end')





