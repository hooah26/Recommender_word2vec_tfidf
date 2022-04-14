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
from PyQt5.QtWidgets import *
from PyQt5 import uic
from job16_buywindow import buywindow

form_secondwindow = uic.loadUiType("./secondwindow.ui")[0] #두 번째창 ui

class secondwindow(QDialog,QWidget,form_secondwindow):
    def __init__(self, mainwindow):
        super(secondwindow,self).__init__()
        self.setupUi(self)
        self.initUI()
        self.show()
        self.mainwindow = mainwindow
        # print(self.mainwindow.recommendation_titles)

    def initUI(self):
        self.btn_close.clicked.connect(self.Close)
        self.btn_buy.clicked.connect(self.buywindow)

    def Close(self):
        self.close()

    def buywindow(self):
        self.hide()  # 메인 윈도우 숨김
        print(self.mainwindow.recommendation_titles)
        self.w = buywindow(self, self.mainwindow)
        self.w.exec()
        self.show()
