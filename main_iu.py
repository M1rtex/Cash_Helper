# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiXFNINt.ui'
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
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 60))
        self.main_header.setMouseTracking(True)
        self.main_header.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(9, 9, 9);\n"
"	border-bottom: 1px solid #000;\n"
"}")
        self.main_header.setFrameShape(QFrame.Box)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_togle = QFrame(self.main_header)
        self.left_menu_togle.setObjectName(u"left_menu_togle")
        self.left_menu_togle.setMaximumSize(QSize(90, 16777215))
        self.left_menu_togle.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 212, 222);\n"
"}")
        self.left_menu_togle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_togle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.left_menu_togle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_men_togle_btn = QPushButton(self.left_menu_togle)
        self.left_men_togle_btn.setObjectName(u"left_men_togle_btn")
        self.left_men_togle_btn.setMinimumSize(QSize(0, 54))
        icon = QIcon()
        icon.addFile(u":/icons/more.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_men_togle_btn.setIcon(icon)
        self.left_men_togle_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.left_men_togle_btn)


        self.horizontalLayout_2.addWidget(self.left_menu_togle)

        self.main_windo_title_bar = QFrame(self.main_header)
        self.main_windo_title_bar.setObjectName(u"main_windo_title_bar")
        self.main_windo_title_bar.setMinimumSize(QSize(0, 0))
        self.main_windo_title_bar.setCursor(QCursor(Qt.ArrowCursor))
        self.main_windo_title_bar.setMouseTracking(True)
        self.main_windo_title_bar.setFrameShape(QFrame.NoFrame)
        self.main_windo_title_bar.setFrameShadow(QFrame.Raised)
        self.main_windo_title_bar.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.main_windo_title_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.main_windo_title_bar)

        self.window_right_btns = QFrame(self.main_header)
        self.window_right_btns.setObjectName(u"window_right_btns")
        self.window_right_btns.setMinimumSize(QSize(100, 60))
        self.window_right_btns.setMaximumSize(QSize(100, 16777215))
        self.window_right_btns.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 212, 222);\n"
"}")
        self.window_right_btns.setFrameShape(QFrame.StyledPanel)
        self.window_right_btns.setFrameShadow(QFrame.Raised)
        self.window_right_btns.setLineWidth(1)
        self.closeButton = QPushButton(self.window_right_btns)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(70, 20, 16, 23))
        self.closeButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QSize(24, 24))
        self.minimizeButton = QPushButton(self.window_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(40, 20, 21, 23))
        self.minimizeButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QSize(22, 22))
        self.restoreButton = QPushButton(self.window_right_btns)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setGeometry(QRect(10, 20, 21, 23))
        self.restoreButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon3)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.window_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(76, 87, 96);\n"
"border: none;")
        self.main_body.setFrameShape(QFrame.WinPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMinimumSize(QSize(0, 460))
        self.left_menu.setMaximumSize(QSize(90, 16777215))
        self.left_menu.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 15px 10px;\n"
"	color: white;\n"
"	background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 212, 222);\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(9, 9, 9);\n"
"}")
        self.left_menu.setFrameShape(QFrame.NoFrame)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setMinimumSize(QSize(0, 0))
        self.left_menu_top_buttons.setFrameShape(QFrame.NoFrame)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.left_menu_top_buttons)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QSize(90, 0))
        self.homeButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.homeButton)

        self.statisticButton = QPushButton(self.left_menu_top_buttons)
        self.statisticButton.setObjectName(u"statisticButton")
        self.statisticButton.setMinimumSize(QSize(90, 0))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Statistic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticButton.setIcon(icon5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.statisticButton)


        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)

        self.settingsButton = QPushButton(self.left_menu)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(90, 0))
        icon6 = QIcon()
        icon6.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.settingsButton)

        self.botto_left_menu_frame = QFrame(self.left_menu)
        self.botto_left_menu_frame.setObjectName(u"botto_left_menu_frame")
        self.botto_left_menu_frame.setMaximumSize(QSize(16777215, 15))
        self.botto_left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.botto_left_menu_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.botto_left_menu_frame)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_body_items = QFrame(self.main_body)
        self.main_body_items.setObjectName(u"main_body_items")
        self.main_body_items.setMinimumSize(QSize(410, 0))
        self.main_body_items.setStyleSheet(u"background-color: rgb(76, 87, 96);")
        self.main_body_items.setFrameShape(QFrame.StyledPanel)
        self.main_body_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_body_items)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.main_body_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Home_form_frame = QFrame(self.home_page)
        self.Home_form_frame.setObjectName(u"Home_form_frame")
        self.Home_form_frame.setMinimumSize(QSize(350, 350))
        self.Home_form_frame.setMaximumSize(QSize(400, 400))
        self.Home_form_frame.setStyleSheet(u"border: 5px solid rgb(7, 7, 7);\n"
"border-radius: 15px;")
        self.Home_form_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Home_form_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Info_image = QFrame(self.Home_form_frame)
        self.Info_image.setObjectName(u"Info_image")
        self.Info_image.setMinimumSize(QSize(100, 100))
        self.Info_image.setMaximumSize(QSize(100, 100))
        self.Info_image.setStyleSheet(u"image: url(:/icons/icons8-user-menu-male-48.png);\n"
"border-radius: 50%;\n"
"border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgb(71, 71, 71);")
        self.Info_image.setFrameShape(QFrame.StyledPanel)
        self.Info_image.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.Info_image, 0, Qt.AlignHCenter)

        self.Info_input_frame = QFrame(self.Home_form_frame)
        self.Info_input_frame.setObjectName(u"Info_input_frame")
        self.Info_input_frame.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"\n"
"QLabel {\n"
"	border: 2px solid rgb(182, 212, 222);\n"
"	border-radius: 10px;\n"
"}")
        self.Info_input_frame.setFrameShape(QFrame.StyledPanel)
        self.Info_input_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.Info_input_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.Salary_lable = QLabel(self.Info_input_frame)
        self.Salary_lable.setObjectName(u"Salary_lable")
        self.Salary_lable.setMinimumSize(QSize(70, 40))
        font = QFont()
        font.setFamily(u"a_Concepto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Salary_lable.setFont(font)
        self.Salary_lable.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.Salary_lable.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Salary_lable)

        self.Salary_lineEdit = QLineEdit(self.Info_input_frame)
        self.Salary_lineEdit.setObjectName(u"Salary_lineEdit")
        self.Salary_lineEdit.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.Salary_lineEdit.setFont(font1)
        self.Salary_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}")
        self.Salary_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.Salary_lineEdit)

        self.Pleasure_lable = QLabel(self.Info_input_frame)
        self.Pleasure_lable.setObjectName(u"Pleasure_lable")
        self.Pleasure_lable.setMinimumSize(QSize(70, 40))
        font2 = QFont()
        font2.setFamily(u"a_Concepto")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.Pleasure_lable.setFont(font2)
        self.Pleasure_lable.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.Pleasure_lable.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Pleasure_lable)

        self.Pleasure_lineEdit = QLineEdit(self.Info_input_frame)
        self.Pleasure_lineEdit.setObjectName(u"Pleasure_lineEdit")
        self.Pleasure_lineEdit.setMinimumSize(QSize(0, 40))
        self.Pleasure_lineEdit.setFont(font1)
        self.Pleasure_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}")
        self.Pleasure_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.Pleasure_lineEdit)

        self.Rest_lable = QLabel(self.Info_input_frame)
        self.Rest_lable.setObjectName(u"Rest_lable")
        self.Rest_lable.setMinimumSize(QSize(70, 40))
        self.Rest_lable.setFont(font)
        self.Rest_lable.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.Rest_lable.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.Rest_lable)

        self.Rest_lineEdit = QLineEdit(self.Info_input_frame)
        self.Rest_lineEdit.setObjectName(u"Rest_lineEdit")
        self.Rest_lineEdit.setMinimumSize(QSize(0, 40))
        self.Rest_lineEdit.setFont(font1)
        self.Rest_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}")
        self.Rest_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.Rest_lineEdit)

        self.Log_lable = QLabel(self.Info_input_frame)
        self.Log_lable.setObjectName(u"Log_lable")
        self.Log_lable.setMinimumSize(QSize(312, 80))
        font3 = QFont()
        font3.setFamily(u"a_Concepto")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.Log_lable.setFont(font3)
        self.Log_lable.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	background-color: rgba(22, 22, 22, 100);\n"
"}")
        self.Log_lable.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.Log_lable)

        self.ConfirmButton = QPushButton(self.Info_input_frame)
        self.ConfirmButton.setObjectName(u"ConfirmButton")
        self.ConfirmButton.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamily(u"a_Concepto")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(True)
        font4.setWeight(75)
        self.ConfirmButton.setFont(font4)
        self.ConfirmButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-color: rgb(54, 111, 197);\n"
"}\n"
"")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.ConfirmButton)


        self.verticalLayout_7.addWidget(self.Info_input_frame)


        self.verticalLayout_4.addWidget(self.Home_form_frame)

        self.stackedWidget.addWidget(self.home_page)
        self.MoreStatistic_page = QWidget()
        self.MoreStatistic_page.setObjectName(u"MoreStatistic_page")
        self.MoreStatistic_page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 15px 10px;\n"
"	color: white;\n"
"	background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 212, 222);\n"
"}")
        self.InfoBars = QFrame(self.MoreStatistic_page)
        self.InfoBars.setObjectName(u"InfoBars")
        self.InfoBars.setGeometry(QRect(9, 9, 371, 411))
        self.InfoBars.setFrameShape(QFrame.NoFrame)
        self.InfoBars.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.InfoBars)
        self.verticalLayout_9.setSpacing(19)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, -1, 9, 9)
        self.InfoPleasureLable = QLabel(self.InfoBars)
        self.InfoPleasureLable.setObjectName(u"InfoPleasureLable")
        self.InfoPleasureLable.setMinimumSize(QSize(140, 50))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.InfoPleasureLable.setFont(font5)
        self.InfoPleasureLable.setStyleSheet(u"background-color: none;\n"
"color: #ffffffff")
        self.InfoPleasureLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.InfoPleasureLable, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.PleasureBar = QProgressBar(self.InfoBars)
        self.PleasureBar.setObjectName(u"PleasureBar")
        self.PleasureBar.setMinimumSize(QSize(350, 0))
        self.PleasureBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 5;\n"
"	background-color: rgb(118, 118, 118);\n"
"	color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 5;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.PleasureBar.setValue(24)
        self.PleasureBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.PleasureBar, 0, Qt.AlignHCenter)

        self.InfoRestLable = QLabel(self.InfoBars)
        self.InfoRestLable.setObjectName(u"InfoRestLable")
        self.InfoRestLable.setMinimumSize(QSize(140, 50))
        self.InfoRestLable.setFont(font5)
        self.InfoRestLable.setStyleSheet(u"background-color: none;\n"
"color: #ffffffff")
        self.InfoRestLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.InfoRestLable, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.RestBar = QProgressBar(self.InfoBars)
        self.RestBar.setObjectName(u"RestBar")
        self.RestBar.setMinimumSize(QSize(350, 0))
        self.RestBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 5;\n"
"	background-color: rgb(118, 118, 118);\n"
"	color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 5;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.RestBar.setValue(24)
        self.RestBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.RestBar, 0, Qt.AlignHCenter)

        self.InfoRemainsLable = QLabel(self.InfoBars)
        self.InfoRemainsLable.setObjectName(u"InfoRemainsLable")
        self.InfoRemainsLable.setMinimumSize(QSize(140, 50))
        self.InfoRemainsLable.setFont(font5)
        self.InfoRemainsLable.setStyleSheet(u"background-color: none;\n"
"color: #ffffffff")
        self.InfoRemainsLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.InfoRemainsLable, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.RemainsBar = QProgressBar(self.InfoBars)
        self.RemainsBar.setObjectName(u"RemainsBar")
        self.RemainsBar.setMinimumSize(QSize(350, 0))
        self.RemainsBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 5;\n"
"	background-color: rgb(118, 118, 118);\n"
"	color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 5;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.RemainsBar.setValue(24)
        self.RemainsBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.RemainsBar, 0, Qt.AlignHCenter)

        self.BackInfoButton = QPushButton(self.InfoBars)
        self.BackInfoButton.setObjectName(u"BackInfoButton")
        self.BackInfoButton.setFont(font5)

        self.verticalLayout_9.addWidget(self.BackInfoButton)

        self.stackedWidget.addWidget(self.MoreStatistic_page)
        self.Statistic_page = QWidget()
        self.Statistic_page.setObjectName(u"Statistic_page")
        self.Statistic_page.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 15px 10px;\n"
"	color: white;\n"
"	background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 212, 222);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.Statistic_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.StatisticBase = QFrame(self.Statistic_page)
        self.StatisticBase.setObjectName(u"StatisticBase")
        self.StatisticBase.setFrameShape(QFrame.StyledPanel)
        self.StatisticBase.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.StatisticBase)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CircularBarBase = QFrame(self.StatisticBase)
        self.CircularBarBase.setObjectName(u"CircularBarBase")
        self.CircularBarBase.setMinimumSize(QSize(350, 350))
        self.CircularBarBase.setFrameShape(QFrame.NoFrame)
        self.CircularBarBase.setFrameShadow(QFrame.Raised)
        self.Container = QFrame(self.CircularBarBase)
        self.Container.setObjectName(u"Container")
        self.Container.setGeometry(QRect(40, 30, 280, 280))
        self.Container.setStyleSheet(u"QFrame {\n"
"	border-radius: 140px;\n"
"	background-color: rgb(122, 142, 149);\n"
"}")
        self.Container.setFrameShape(QFrame.NoFrame)
        self.Container.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.Container)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 251, 271))
        self.frame.setMinimumSize(QSize(145, 0))
        self.frame.setStyleSheet(u"background-color: none;")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.coastsPercent = QLabel(self.frame)
        self.coastsPercent.setObjectName(u"coastsPercent")
        font6 = QFont()
        font6.setFamily(u"a_Concepto")
        font6.setPointSize(30)
        self.coastsPercent.setFont(font6)
        self.coastsPercent.setStyleSheet(u"background-color: none;\n"
"color:#ffffffff")
        self.coastsPercent.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.coastsPercent, 2, 0, 1, 1)

        self.coastsConLable2 = QLabel(self.frame)
        self.coastsConLable2.setObjectName(u"coastsConLable2")
        self.coastsConLable2.setFont(font5)
        self.coastsConLable2.setStyleSheet(u"background-color: none;\n"
"color: #ffffffff")
        self.coastsConLable2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.coastsConLable2, 3, 0, 1, 1)

        self.coastsConLable = QLabel(self.frame)
        self.coastsConLable.setObjectName(u"coastsConLable")
        self.coastsConLable.setMinimumSize(QSize(140, 50))
        self.coastsConLable.setFont(font5)
        self.coastsConLable.setStyleSheet(u"background-color: none;\n"
"color: #ffffffff")
        self.coastsConLable.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.coastsConLable, 1, 0, 1, 1)

        self.CircularBG = QFrame(self.CircularBarBase)
        self.CircularBG.setObjectName(u"CircularBG")
        self.CircularBG.setGeometry(QRect(30, 20, 300, 300))
        self.CircularBG.setStyleSheet(u"QFrame {\n"
"	border-radius: 150;\n"
"	background-color: rgba(127, 127, 127, 110);\n"
"}")
        self.CircularBG.setFrameShape(QFrame.NoFrame)
        self.CircularBG.setFrameShadow(QFrame.Raised)
        self.CircularProgress = QFrame(self.CircularBarBase)
        self.CircularProgress.setObjectName(u"CircularProgress")
        self.CircularProgress.setGeometry(QRect(30, 20, 300, 300))
        self.CircularProgress.setMinimumSize(QSize(100, 100))
        self.CircularProgress.setMaximumSize(QSize(300, 300))
        self.CircularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(34, 0, 146, 0), stop:0.750 rgba(158, 158, 158, 255));\n"
"}")
        self.CircularProgress.setFrameShape(QFrame.NoFrame)
        self.CircularProgress.setFrameShadow(QFrame.Raised)
        self.CircularBG.raise_()
        self.CircularProgress.raise_()
        self.Container.raise_()

        self.verticalLayout_8.addWidget(self.CircularBarBase, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.MoreInfoButton = QPushButton(self.StatisticBase)
        self.MoreInfoButton.setObjectName(u"MoreInfoButton")
        self.MoreInfoButton.setFont(font5)

        self.verticalLayout_8.addWidget(self.MoreInfoButton)


        self.verticalLayout_5.addWidget(self.StatisticBase)

        self.stackedWidget.addWidget(self.Statistic_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_6 = QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.settingsBar = QFrame(self.settings_page)
        self.settingsBar.setObjectName(u"settingsBar")
        self.settingsBar.setStyleSheet(u"")
        self.settingsBar.setFrameShape(QFrame.NoFrame)
        self.settingsBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.settingsBar)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ChangeCurrencyBar = QFrame(self.settingsBar)
        self.ChangeCurrencyBar.setObjectName(u"ChangeCurrencyBar")
        self.ChangeCurrencyBar.setMaximumSize(QSize(16777215, 150))
        self.ChangeCurrencyBar.setStyleSheet(u"QFrame {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 20;\n"
"}")
        self.ChangeCurrencyBar.setFrameShape(QFrame.StyledPanel)
        self.ChangeCurrencyBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.ChangeCurrencyBar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ChangeLabel = QLabel(self.ChangeCurrencyBar)
        self.ChangeLabel.setObjectName(u"ChangeLabel")
        font7 = QFont()
        font7.setFamily(u"a_Concepto")
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setItalic(True)
        font7.setWeight(75)
        self.ChangeLabel.setFont(font7)
        self.ChangeLabel.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgba(255, 255, 255, 0);\n"
"}")
        self.ChangeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.ChangeLabel)

        self.CurrencyBox = QComboBox(self.ChangeCurrencyBar)
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.setObjectName(u"CurrencyBox")
        self.CurrencyBox.setFont(font1)
        self.CurrencyBox.setStyleSheet(u"QComboBox {\n"
"	color:white;\n"
"	border: 2px solid rgb(182, 212, 222);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border-color:  rgb(54, 111, 197);\n"
"}")

        self.verticalLayout_10.addWidget(self.CurrencyBox)

        self.SettingsConfirmButton = QPushButton(self.ChangeCurrencyBar)
        self.SettingsConfirmButton.setObjectName(u"SettingsConfirmButton")
        self.SettingsConfirmButton.setMinimumSize(QSize(300, 30))
        self.SettingsConfirmButton.setFont(font7)
        self.SettingsConfirmButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-color: rgb(54, 111, 197);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.SettingsConfirmButton)


        self.verticalLayout_11.addWidget(self.ChangeCurrencyBar)

        self.frame_2 = QFrame(self.settingsBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 160))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 20;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(330, 60))
        self.label.setFont(font7)
        self.label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgba(255, 255, 255, 0);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label)

        self.SaveAgainButton = QPushButton(self.frame_2)
        self.SaveAgainButton.setObjectName(u"SaveAgainButton")
        self.SaveAgainButton.setMinimumSize(QSize(300, 30))
        self.SaveAgainButton.setFont(font4)
        self.SaveAgainButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-color: rgb(54, 111, 197);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.SaveAgainButton)

        self.ClearLOGButton = QPushButton(self.frame_2)
        self.ClearLOGButton.setObjectName(u"ClearLOGButton")
        self.ClearLOGButton.setMinimumSize(QSize(300, 30))
        self.ClearLOGButton.setFont(font4)
        self.ClearLOGButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-color: rgb(54, 111, 197);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.ClearLOGButton)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.settingsBar)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_3.addWidget(self.stackedWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.main_body_items)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_men_togle_btn.setText("")
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.statisticButton.setText(QCoreApplication.translate("MainWindow", u"STATISTIC", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.Salary_lable.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.Salary_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430", None))
        self.Pleasure_lable.setText(QCoreApplication.translate("MainWindow", u"Pleasure", None))
        self.Pleasure_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.Rest_lable.setText(QCoreApplication.translate("MainWindow", u"Rest", None))
        self.Rest_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.Log_lable.setText("")
        self.ConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.InfoPleasureLable.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Pleasure costs</span></p>", None))
        self.InfoRestLable.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Rest costs</span></p>", None))
        self.InfoRemainsLable.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Remains</span></p>", None))
        self.BackInfoButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.coastsPercent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:72pt;\">0%</span></p></body></html>", None))
        self.coastsConLable2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">from </span><span style=\" font-size:16pt; font-weight:600; color:#000000;\">YOUR</span><span style=\" font-size:16pt;\"> salary</span></p></body></html>", None))
        self.coastsConLable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR</span><span style=\" font-size:18pt; font-weight:600; color:#67ebff;\"/><span style=\" font-size:18pt;\">costs</span></p></body></html>", None))
        self.MoreInfoButton.setText(QCoreApplication.translate("MainWindow", u"MORE", None))
        self.ChangeLabel.setText(QCoreApplication.translate("MainWindow", u"Change currency", None))
        self.CurrencyBox.setItemText(0, QCoreApplication.translate("MainWindow", u"RUB", None))
        self.CurrencyBox.setItemText(1, QCoreApplication.translate("MainWindow", u"EUR", None))
        self.CurrencyBox.setItemText(2, QCoreApplication.translate("MainWindow", u"USD", None))
        self.CurrencyBox.setItemText(3, QCoreApplication.translate("MainWindow", u"KZT", None))
        self.CurrencyBox.setItemText(4, QCoreApplication.translate("MainWindow", u"UAH", None))
        self.CurrencyBox.setItemText(5, QCoreApplication.translate("MainWindow", u"GBP", None))
        self.CurrencyBox.setItemText(6, QCoreApplication.translate("MainWindow", u"PLN", None))

        self.SettingsConfirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Misc", None))
        self.SaveAgainButton.setText(QCoreApplication.translate("MainWindow", u"Save exel again", None))
        self.ClearLOGButton.setText(QCoreApplication.translate("MainWindow", u"Clear LOG", None))
    # retranslateUi

