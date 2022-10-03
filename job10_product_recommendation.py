import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle
from gensim.models import Word2Vec

df_reviews = pd.read_csv('./crawling_data/onesentence.csv')
df_reviews.info()
def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    print(len(simScore))
    print(simScore)
    simScore = sorted(simScore, key=lambda x:x[1],
                      reverse=True)
    simScore = simScore[1:11]
    movieidx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[movieidx]
    return recMovieList.iloc[:, 0]

Tfidf_matrix = mmread('./models/drink.mtx').tocsr()
with open('./models/drink.pickle', 'rb') as f:
    Tfidf = pickle.load(f)


embedding_model = Word2Vec.load('./models/drink_word2vecModel.model')
key_word = '게토레이'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
sentence = [key_word] * 11
words = []
for word, _ in sim_word:
    words.append(word)
for i, word in enumerate(words):
    sentence += [word] * (10 - i)

sentence = ' '.join(sentence)

# 문장을 이용
sentence = '게토레이 레몬'

sentence_vec = Tfidf.transform([sentence])
cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)

# cosine_sim = linear_kernel(Tfidf_matrix[movie_idx], Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)

print(recommendation)












