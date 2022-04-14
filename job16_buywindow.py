import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import requests
import urllib
import webbrowser

form_buywindow = uic.loadUiType("buywindow.ui")[0] #두 번째창 ui
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}

class buywindow(QDialog,QWidget,form_buywindow):
    def __init__(self, secondwindow, mainwindow):
        super(buywindow,self).__init__()
        self.setupUi(self)
        self.seconwindow = secondwindow
        self.mainwindow = mainwindow
        self.initUI()
        self.show()
        self.btn_back.clicked.connect(self.Close)
        self.btn_more.clicked.connect(self.More)

    def initUI(self):
        self.setupUi(self)
        self.lbl_img.setPixmap(QPixmap('buy.jpg'))
        self.lbl_ai.setPixmap(QPixmap('ai.jpg'))
        # print(self.mainwindow.recommendation_titles[0])
        self.title = self.mainwindow.recommendation_titles.split('\n')


    def More(self):
        self.names = []
        for i in range(3):
            self.names.append(self.title[i])
        print(self.names)
        self.lbl_pn1.setText(self.title[0])
        self.lbl_pn2.setText(self.title[1])
        self.lbl_pn3.setText(self.title[2])
        imgs = []
        hrefs = []

        for name in self.names :
            url = 'https://www.coupang.com/np/search?component=&q={}&channel=user'.format(name)
            try:
                res = requests.get(url, headers=headers, timeout=10)
                print('서버확인')
                soup = BeautifulSoup(res.text, 'html.parser')
                img = soup.find("img", {"class": "search-product-wrap-img"})['src']
                href = soup.find('a', {'class': 'search-product-link'})['href']
                product_name = soup.find('div', {'class': 'name'}).get_text()
                URL = 'https:' + img
                href_URL = 'https://www.coupang.com/' + href
                imgs.append(URL)
                hrefs.append(href_URL)
            except:
                print('쿠팡서버 거절')
                continue
        print('포문끝')
        print(imgs)
        print(hrefs)
        # try:
        #     for i in range(1,4):
        #         self.btn_buy[i].setText('당장구매하기',i)
        #         self.btn_buy[i].clicked.connect(lambda: webbrowser.open(hrefs[i]))
        # except:
        #     print('값이 없음')
        # print('링크끝')

        # self.img_url1 = imgs[0]
        # self.img_url2 = imgs[1]
        # self.img_url3 = imgs[2]
        # self.img1 = urllib.request.urlopen(self.img_url1).read()
        # self.img2 = urllib.request.urlopen(self.img_url2).read()
        # self.img3 = urllib.request.urlopen(self.img_url3).read()
        # self.pixmap1.loadFromData(self.img1)
        # self.pixmap2.loadFromData(self.img2)
        # self.pixmap3.loadFromData(self.img3)
        # self.lbl_pd1.setPixmap(self.pixmap1)
        # self.lbl_pd2.setPixmap(self.pixmap2)
        # self.lbl_pd3.setPixmap(self.pixmap3)
        #
        print('이미지끝')


    def Close(self):
        self.close()


