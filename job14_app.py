import sys
from PyQt5.QtWidgets import *
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread, mmwrite
import pickle
from PyQt5 import uic
from gensim.models import Word2Vec
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from job15_secondwindow import secondwindow

form_window = uic.loadUiType('./mainWidget.ui')[0]
form_secondwindow = uic.loadUiType("./secondwindow.ui")[0] #두 번째창 ui
form_buywindow = uic.loadUiType("./buywindow.ui")[0] #두 번째창 ui

class Exam(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.lbl_coupang.setPixmap(QPixmap('C:\work\python\drink_recommendations_t\couang.png').scaledToWidth(500))
        self.category = ['음료', '가공식품', '과자', '커피,원두,차', '냉장,냉동,간편요리', '건강 식품']
        self.df_reviews = pd.read_csv('models/drink_onesentence.csv')
        self.Tfidf_matrix = mmread('./models/drink.mtx').tocsr()
        with open('./models/drink.pickle', 'rb') as f:
            self.Tfidf = pickle.load(f)
        for i in self.category :
            self.cmb_category.addItem(i)
        self.cmb_category.currentIndexChanged.connect(self.cmb_category_slot)

        self.btn_search.clicked.connect(self.btn_search_slot)
        # self.btn_search.clicked.connect(self.window)

    def btn_search_slot(self):
        sentence = self.le_keyword.text()
        self.text = sentence
        # print(sentence)

        input_words = sentence.split()
        if len(input_words) >= 10:
            sentence_vec = self.Tfidf.transform([sentence])
            cosine_sim = linear_kernel(sentence_vec, self.Tfidf_matrix)
            recommendation_titles = self.recommend_by_sentence(sentence)
            self.lbl_recommend.setText(recommendation_titles)

        else:
            key_word = input_words[0]
            embedding_model = Word2Vec.load('./models/drink_word2vecModel.model')
            try:
                sim_word = embedding_model.wv.most_similar(key_word, topn=10)
            except:
                self.lbl_recommend.setText('제가 모르는 단어에요 ㅠㅠ')
                return
            sentence = [key_word] * 11
            words = []
            for word, _ in sim_word:
                words.append(word)
            for i, word in enumerate(words):
                sentence += [word] * (10 - i)

            sentence = ' '.join(sentence)
            self.recommendation_titles = self.recommend_by_sentence(sentence)
            print(len(self.recommendation_titles))
            print(self.text)
            self.hide()
            self.sec = secondwindow(self)
            self.sec.exec()
            self.show()




    def recommend_by_sentence(self, sentence):
        sentence_vec = self.Tfidf.transform([sentence])
        cosine_sim = linear_kernel(sentence_vec, self.Tfidf_matrix)
        recommendation_titles = self.getRecommendation(cosine_sim)
        recommendation_titles = '\n'.join(list(recommendation_titles))
        return recommendation_titles



    def cmb_category_slot(self):
        category = self.cmb_category.currentText()
        self.lbl_title.setText(category)

    def getRecommendation(self, cosine_sim):
        simScore = list(enumerate(cosine_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1],
                          reverse=True)
        simScore = simScore[1:11]
        movieidx = [i[0] for i in simScore]
        recMovieList = self.df_reviews.iloc[movieidx]
        return recMovieList.iloc[:, 0]



app = QApplication(sys.argv)
mainWindow = Exam()

mainWindow.show()

sys.exit(app.exec_())