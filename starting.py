# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startingWrTyLC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(46, 48, 79);\n"
"	color: rgb(220,220,220);\n"
"	border-radius: 10;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nameLable = QLabel(self.frame)
        self.nameLable.setObjectName(u"nameLable")
        self.nameLable.setGeometry(QRect(0, 30, 481, 61))
        font = QFont()
        font.setFamily(u"a_Concepto")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nameLable.setFont(font)
        self.nameLable.setAlignment(Qt.AlignCenter)
        self.descriptionLable = QLabel(self.frame)
        self.descriptionLable.setObjectName(u"descriptionLable")
        self.descriptionLable.setGeometry(QRect(0, 80, 481, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.descriptionLable.setFont(font1)
        self.descriptionLable.setStyleSheet(u"color: rgb(158, 158, 158)")
        self.descriptionLable.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(5, 201, 471, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(73, 77, 126);\n"
"	color: rgb(140,140,140);\n"
"	border-style: none;\n"
"	border-radius: 10;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 10;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.loadingLable = QLabel(self.frame)
        self.loadingLable.setObjectName(u"loadingLable")
        self.loadingLable.setGeometry(QRect(0, 230, 481, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.loadingLable.setFont(font2)
        self.loadingLable.setStyleSheet(u"color: rgb(158, 158, 158)")
        self.loadingLable.setAlignment(Qt.AlignCenter)
        self.creditsLable = QLabel(self.frame)
        self.creditsLable.setObjectName(u"creditsLable")
        self.creditsLable.setGeometry(QRect(5, 255, 471, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.creditsLable.setFont(font3)
        self.creditsLable.setStyleSheet(u"color: rgb(158, 158, 158)")
        self.creditsLable.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameLable.setText(QCoreApplication.translate("MainWindow", u"<strong>Cash Helper</strong>", None))
        self.descriptionLable.setText(QCoreApplication.translate("MainWindow", u"<strong>Help</strong> with <strong>using money</strong>", None))
        self.loadingLable.setText(QCoreApplication.translate("MainWindow", u"loading...", None))
        self.creditsLable.setText(QCoreApplication.translate("MainWindow", u"<strong>Created:</strong> M1rtex", None))
    # retranslateUi

