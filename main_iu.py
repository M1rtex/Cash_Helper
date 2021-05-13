from PyQt5 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-radius: 5px;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 60))
        self.main_header.setMouseTracking(True)
        self.main_header.setStyleSheet("QFrame {\n"
"    background-color: rgb(9, 9, 9);\n"
"    border-bottom: 1px solid #000;\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.Box)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_menu_togle = QtWidgets.QFrame(self.main_header)
        self.left_menu_togle.setMaximumSize(QtCore.QSize(90, 16777215))
        self.left_menu_togle.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(182, 212, 222);\n"
"}")
        self.left_menu_togle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_togle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_togle.setObjectName("left_menu_togle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_menu_togle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_men_togle_btn = QtWidgets.QPushButton(self.left_menu_togle)
        self.left_men_togle_btn.setMinimumSize(QtCore.QSize(0, 54))
        self.left_men_togle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_men_togle_btn.setIcon(icon)
        self.left_men_togle_btn.setIconSize(QtCore.QSize(24, 24))
        self.left_men_togle_btn.setObjectName("left_men_togle_btn")
        self.horizontalLayout_3.addWidget(self.left_men_togle_btn)
        self.horizontalLayout_2.addWidget(self.left_menu_togle)
        self.main_windo_title_bar = QtWidgets.QFrame(self.main_header)
        self.main_windo_title_bar.setMinimumSize(QtCore.QSize(0, 0))
        self.main_windo_title_bar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.main_windo_title_bar.setMouseTracking(True)
        self.main_windo_title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_windo_title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_windo_title_bar.setLineWidth(0)
        self.main_windo_title_bar.setObjectName("main_windo_title_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.main_windo_title_bar)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2.addWidget(self.main_windo_title_bar)
        self.window_right_btns = QtWidgets.QFrame(self.main_header)
        self.window_right_btns.setMinimumSize(QtCore.QSize(100, 60))
        self.window_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.window_right_btns.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(182, 212, 222);\n"
"}")
        self.window_right_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_right_btns.setLineWidth(1)
        self.window_right_btns.setObjectName("window_right_btns")
        self.closeButton = QtWidgets.QPushButton(self.window_right_btns)
        self.closeButton.setGeometry(QtCore.QRect(70, 20, 21, 23))
        self.closeButton.setStyleSheet("")
        self.closeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.window_right_btns)
        self.minimizeButton.setGeometry(QtCore.QRect(40, 20, 21, 23))
        self.minimizeButton.setStyleSheet("")
        self.minimizeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QtCore.QSize(22, 22))
        self.minimizeButton.setObjectName("minimizeButton")
        self.restoreButton = QtWidgets.QPushButton(self.window_right_btns)
        self.restoreButton.setGeometry(QtCore.QRect(10, 20, 21, 23))
        self.restoreButton.setStyleSheet("")
        self.restoreButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon3)
        self.restoreButton.setIconSize(QtCore.QSize(24, 24))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_2.addWidget(self.window_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("background-color: rgb(76, 87, 96);\n"
"border: none;")
        self.main_body.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMinimumSize(QtCore.QSize(0, 460))
        self.left_menu.setMaximumSize(QtCore.QSize(90, 16777215))
        self.left_menu.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 15px 10px;\n"
"    color: white;\n"
"    background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(182, 212, 222);\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: rgb(9, 9, 9);\n"
"}")
        self.left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setObjectName("left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.left_menu)
        self.left_menu_top_buttons.setMinimumSize(QtCore.QSize(0, 0))
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.homeButton = QtWidgets.QPushButton(self.left_menu_top_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QtCore.QSize(90, 0))
        self.homeButton.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setObjectName("homeButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.homeButton)
        self.statisticButton = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.statisticButton.setMinimumSize(QtCore.QSize(90, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Statistic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statisticButton.setIcon(icon5)
        self.statisticButton.setObjectName("statisticButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.statisticButton)
        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)
        self.settingsButton = QtWidgets.QPushButton(self.left_menu)
        self.settingsButton.setMinimumSize(QtCore.QSize(90, 0))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon6)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout_2.addWidget(self.settingsButton)
        self.botto_left_menu_frame = QtWidgets.QFrame(self.left_menu)
        self.botto_left_menu_frame.setMaximumSize(QtCore.QSize(16777215, 15))
        self.botto_left_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botto_left_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botto_left_menu_frame.setObjectName("botto_left_menu_frame")
        self.verticalLayout_2.addWidget(self.botto_left_menu_frame)
        self.horizontalLayout.addWidget(self.left_menu)
        self.main_body_items = QtWidgets.QFrame(self.main_body)
        self.main_body_items.setMinimumSize(QtCore.QSize(410, 0))
        self.main_body_items.setStyleSheet("background-color: rgb(76, 87, 96);")
        self.main_body_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_items.setObjectName("main_body_items")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_body_items)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body_items)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Home_form_frame = QtWidgets.QFrame(self.home_page)
        self.Home_form_frame.setMinimumSize(QtCore.QSize(350, 350))
        self.Home_form_frame.setMaximumSize(QtCore.QSize(400, 400))
        self.Home_form_frame.setStyleSheet("border: 5px solid rgb(7, 7, 7);\n"
"border-radius: 15px;")
        self.Home_form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_form_frame.setObjectName("Home_form_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Home_form_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Info_image = QtWidgets.QFrame(self.Home_form_frame)
        self.Info_image.setMinimumSize(QtCore.QSize(100, 100))
        self.Info_image.setMaximumSize(QtCore.QSize(100, 100))
        self.Info_image.setStyleSheet("image: url(:/icons/icons8-user-menu-male-48.png);\n"
"border-radius: 50%;\n"
"border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgb(71, 71, 71);")
        self.Info_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_image.setObjectName("Info_image")
        self.verticalLayout_7.addWidget(self.Info_image, 0, QtCore.Qt.AlignHCenter)
        self.Info_input_frame = QtWidgets.QFrame(self.Home_form_frame)
        self.Info_input_frame.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"\n"
"QLabel {\n"
"    border: 2px solid rgb(182, 212, 222);\n"
"    border-radius: 10px;\n"
"}")
        self.Info_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_input_frame.setObjectName("Info_input_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Info_input_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Salary_lable = QtWidgets.QLabel(self.Info_input_frame)
        self.Salary_lable.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Salary_lable.setFont(font)
        self.Salary_lable.setStyleSheet("QLabel {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Salary_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Salary_lable.setObjectName("Salary_lable")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Salary_lable)
        self.Salary_lineEdit = QtWidgets.QLineEdit(self.Info_input_frame)
        self.Salary_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Salary_lineEdit.setFont(font)
        self.Salary_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}")
        self.Salary_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Salary_lineEdit.setObjectName("Salary_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Salary_lineEdit)
        self.Pleasure_lable = QtWidgets.QLabel(self.Info_input_frame)
        self.Pleasure_lable.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Pleasure_lable.setFont(font)
        self.Pleasure_lable.setStyleSheet("QLabel {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Pleasure_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Pleasure_lable.setObjectName("Pleasure_lable")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Pleasure_lable)
        self.Pleasure_lineEdit = QtWidgets.QLineEdit(self.Info_input_frame)
        self.Pleasure_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pleasure_lineEdit.setFont(font)
        self.Pleasure_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}")
        self.Pleasure_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Pleasure_lineEdit.setObjectName("Pleasure_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Pleasure_lineEdit)
        self.Rest_lable = QtWidgets.QLabel(self.Info_input_frame)
        self.Rest_lable.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Rest_lable.setFont(font)
        self.Rest_lable.setStyleSheet("QLabel {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Rest_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Rest_lable.setObjectName("Rest_lable")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Rest_lable)
        self.Rest_lineEdit = QtWidgets.QLineEdit(self.Info_input_frame)
        self.Rest_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Rest_lineEdit.setFont(font)
        self.Rest_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}")
        self.Rest_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Rest_lineEdit.setObjectName("Rest_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Rest_lineEdit)
        self.Log_lable = QtWidgets.QLabel(self.Info_input_frame)
        self.Log_lable.setMinimumSize(QtCore.QSize(312, 80))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Log_lable.setFont(font)
        self.Log_lable.setStyleSheet("QLabel {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    background-color: rgba(22, 22, 22, 100);\n"
"}")
        self.Log_lable.setText("")
        self.Log_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.Log_lable.setObjectName("Log_lable")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.Log_lable)
        self.ConfirmButton = QtWidgets.QPushButton(self.Info_input_frame)
        self.ConfirmButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(54, 111, 197);\n"
"}\n"
"")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.ConfirmButton)
        self.verticalLayout_7.addWidget(self.Info_input_frame)
        self.verticalLayout_4.addWidget(self.Home_form_frame)
        self.stackedWidget.addWidget(self.home_page)
        self.MoreStatistic_page = QtWidgets.QWidget()
        self.MoreStatistic_page.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 15px 10px;\n"
"    color: white;\n"
"    background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(182, 212, 222);\n"
"}")
        self.MoreStatistic_page.setObjectName("MoreStatistic_page")
        self.InfoBars = QtWidgets.QFrame(self.MoreStatistic_page)
        self.InfoBars.setGeometry(QtCore.QRect(9, 9, 371, 411))
        self.InfoBars.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.InfoBars.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InfoBars.setObjectName("InfoBars")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.InfoBars)
        self.verticalLayout_9.setContentsMargins(9, -1, 9, 9)
        self.verticalLayout_9.setSpacing(19)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.InfoPleasureLable = QtWidgets.QLabel(self.InfoBars)
        self.InfoPleasureLable.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.InfoPleasureLable.setFont(font)
        self.InfoPleasureLable.setStyleSheet("background-color: none;\n"
"color: #ffffffff")
        self.InfoPleasureLable.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoPleasureLable.setObjectName("InfoPleasureLable")
        self.verticalLayout_9.addWidget(self.InfoPleasureLable, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PleasureBar = QtWidgets.QProgressBar(self.InfoBars)
        self.PleasureBar.setMinimumSize(QtCore.QSize(350, 0))
        self.PleasureBar.setStyleSheet("QProgressBar{\n"
"    border-radius: 5;\n"
"    background-color: rgb(118, 118, 118);\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 5;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.PleasureBar.setProperty("value", 24)
        self.PleasureBar.setAlignment(QtCore.Qt.AlignCenter)
        self.PleasureBar.setObjectName("PleasureBar")
        self.verticalLayout_9.addWidget(self.PleasureBar, 0, QtCore.Qt.AlignHCenter)
        self.InfoRestLable = QtWidgets.QLabel(self.InfoBars)
        self.InfoRestLable.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.InfoRestLable.setFont(font)
        self.InfoRestLable.setStyleSheet("background-color: none;\n"
"color: #ffffffff")
        self.InfoRestLable.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoRestLable.setObjectName("InfoRestLable")
        self.verticalLayout_9.addWidget(self.InfoRestLable, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RestBar = QtWidgets.QProgressBar(self.InfoBars)
        self.RestBar.setMinimumSize(QtCore.QSize(350, 0))
        self.RestBar.setStyleSheet("QProgressBar{\n"
"    border-radius: 5;\n"
"    background-color: rgb(118, 118, 118);\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 5;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.RestBar.setProperty("value", 24)
        self.RestBar.setAlignment(QtCore.Qt.AlignCenter)
        self.RestBar.setObjectName("RestBar")
        self.verticalLayout_9.addWidget(self.RestBar, 0, QtCore.Qt.AlignHCenter)
        self.InfoRemainsLable = QtWidgets.QLabel(self.InfoBars)
        self.InfoRemainsLable.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.InfoRemainsLable.setFont(font)
        self.InfoRemainsLable.setStyleSheet("background-color: none;\n"
"color: #ffffffff")
        self.InfoRemainsLable.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoRemainsLable.setObjectName("InfoRemainsLable")
        self.verticalLayout_9.addWidget(self.InfoRemainsLable, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RemainsBar = QtWidgets.QProgressBar(self.InfoBars)
        self.RemainsBar.setMinimumSize(QtCore.QSize(350, 0))
        self.RemainsBar.setStyleSheet("QProgressBar{\n"
"    border-radius: 5;\n"
"    background-color: rgb(118, 118, 118);\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 5;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(133, 134, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.RemainsBar.setProperty("value", 24)
        self.RemainsBar.setAlignment(QtCore.Qt.AlignCenter)
        self.RemainsBar.setObjectName("RemainsBar")
        self.verticalLayout_9.addWidget(self.RemainsBar, 0, QtCore.Qt.AlignHCenter)
        self.BackInfoButton = QtWidgets.QPushButton(self.InfoBars)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.BackInfoButton.setFont(font)
        self.BackInfoButton.setObjectName("BackInfoButton")
        self.verticalLayout_9.addWidget(self.BackInfoButton)
        self.stackedWidget.addWidget(self.MoreStatistic_page)
        self.Statistic_page = QtWidgets.QWidget()
        self.Statistic_page.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 15px 10px;\n"
"    color: white;\n"
"    background-color: rgb(29, 29, 29);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(182, 212, 222);\n"
"}")
        self.Statistic_page.setObjectName("Statistic_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Statistic_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.StatisticBase = QtWidgets.QFrame(self.Statistic_page)
        self.StatisticBase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StatisticBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StatisticBase.setObjectName("StatisticBase")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.StatisticBase)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.CircularBarBase = QtWidgets.QFrame(self.StatisticBase)
        self.CircularBarBase.setMinimumSize(QtCore.QSize(350, 350))
        self.CircularBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CircularBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularBarBase.setObjectName("CircularBarBase")
        self.Container = QtWidgets.QFrame(self.CircularBarBase)
        self.Container.setGeometry(QtCore.QRect(40, 30, 280, 280))
        self.Container.setStyleSheet("QFrame {\n"
"    border-radius: 140px;\n"
"    background-color: rgb(122, 142, 149);\n"
"}")
        self.Container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        self.frame = QtWidgets.QFrame(self.Container)
        self.frame.setGeometry(QtCore.QRect(10, 0, 251, 271))
        self.frame.setMinimumSize(QtCore.QSize(145, 0))
        self.frame.setStyleSheet("background-color: none;")
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.coastsPercent = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(30)
        self.coastsPercent.setFont(font)
        self.coastsPercent.setStyleSheet("background-color: none;\n"
"color:#ffffffff")
        self.coastsPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.coastsPercent.setObjectName("coastsPercent")
        self.gridLayout.addWidget(self.coastsPercent, 2, 0, 1, 1)
        self.coastsConLable2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.coastsConLable2.setFont(font)
        self.coastsConLable2.setStyleSheet("background-color: none;\n"
"color: #ffffffff")
        self.coastsConLable2.setAlignment(QtCore.Qt.AlignCenter)
        self.coastsConLable2.setObjectName("coastsConLable2")
        self.gridLayout.addWidget(self.coastsConLable2, 3, 0, 1, 1)
        self.coastsConLable = QtWidgets.QLabel(self.frame)
        self.coastsConLable.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.coastsConLable.setFont(font)
        self.coastsConLable.setStyleSheet("background-color: none;\n"
"color: #ffffffff")
        self.coastsConLable.setAlignment(QtCore.Qt.AlignCenter)
        self.coastsConLable.setObjectName("coastsConLable")
        self.gridLayout.addWidget(self.coastsConLable, 1, 0, 1, 1)
        self.CircularBG = QtWidgets.QFrame(self.CircularBarBase)
        self.CircularBG.setGeometry(QtCore.QRect(30, 20, 300, 300))
        self.CircularBG.setStyleSheet("QFrame {\n"
"    border-radius: 150;\n"
"    background-color: rgba(127, 127, 127, 110);\n"
"}")
        self.CircularBG.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CircularBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularBG.setObjectName("CircularBG")
        self.CircularProgress = QtWidgets.QFrame(self.CircularBarBase)
        self.CircularProgress.setGeometry(QtCore.QRect(30, 20, 300, 300))
        self.CircularProgress.setMinimumSize(QtCore.QSize(100, 100))
        self.CircularProgress.setMaximumSize(QtCore.QSize(300, 300))
        self.CircularProgress.setStyleSheet("QFrame {\n"
"    border-radius: 150;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(34, 0, 146, 0), stop:0.750 rgba(158, 158, 158, 255));\n"
"}")
        self.CircularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CircularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularProgress.setObjectName("CircularProgress")
        self.CircularBG.raise_()
        self.CircularProgress.raise_()
        self.Container.raise_()
        self.verticalLayout_8.addWidget(self.CircularBarBase, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.MoreInfoButton = QtWidgets.QPushButton(self.StatisticBase)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.MoreInfoButton.setFont(font)
        self.MoreInfoButton.setObjectName("MoreInfoButton")
        self.verticalLayout_8.addWidget(self.MoreInfoButton)
        self.verticalLayout_5.addWidget(self.StatisticBase)
        self.stackedWidget.addWidget(self.Statistic_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.settingsBar = QtWidgets.QFrame(self.settings_page)
        self.settingsBar.setStyleSheet("")
        self.settingsBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsBar.setObjectName("settingsBar")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.settingsBar)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.ChangeCurrencyBar = QtWidgets.QFrame(self.settingsBar)
        self.ChangeCurrencyBar.setMaximumSize(QtCore.QSize(16777215, 150))
        self.ChangeCurrencyBar.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 20;\n"
"}")
        self.ChangeCurrencyBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ChangeCurrencyBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ChangeCurrencyBar.setObjectName("ChangeCurrencyBar")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.ChangeCurrencyBar)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.ChangeLabel = QtWidgets.QLabel(self.ChangeCurrencyBar)
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ChangeLabel.setFont(font)
        self.ChangeLabel.setStyleSheet("QLabel {\n"
"    border: 1px solid rgba(255, 255, 255, 0);\n"
"}")
        self.ChangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangeLabel.setObjectName("ChangeLabel")
        self.verticalLayout_10.addWidget(self.ChangeLabel)
        self.CurrencyBox = QtWidgets.QComboBox(self.ChangeCurrencyBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrencyBox.setFont(font)
        self.CurrencyBox.setStyleSheet("QComboBox {\n"
"    color:white;\n"
"    border: 2px solid rgb(182, 212, 222);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color:  rgb(54, 111, 197);\n"
"}")
        self.CurrencyBox.setObjectName("CurrencyBox")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.verticalLayout_10.addWidget(self.CurrencyBox)
        self.SettingsConfirmButton = QtWidgets.QPushButton(self.ChangeCurrencyBar)
        self.SettingsConfirmButton.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SettingsConfirmButton.setFont(font)
        self.SettingsConfirmButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(54, 111, 197);\n"
"}\n"
"")
        self.SettingsConfirmButton.setObjectName("SettingsConfirmButton")
        self.verticalLayout_10.addWidget(self.SettingsConfirmButton)
        self.verticalLayout_11.addWidget(self.ChangeCurrencyBar)
        self.ClearLOGButton = QtWidgets.QPushButton(self.settingsBar)
        self.ClearLOGButton.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("a_Concepto")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ClearLOGButton.setFont(font)
        self.ClearLOGButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-color: rgb(90, 152, 206);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-color: rgb(54, 111, 197);\n"
"}\n"
"")
        self.ClearLOGButton.setObjectName("ClearLOGButton")
        self.verticalLayout_11.addWidget(self.ClearLOGButton)
        self.verticalLayout_6.addWidget(self.settingsBar)
        self.stackedWidget.addWidget(self.settings_page)
        self.verticalLayout_3.addWidget(self.stackedWidget, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.main_body_items)
        self.verticalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.statisticButton.setText(_translate("MainWindow", "STATISTIC"))
        self.settingsButton.setText(_translate("MainWindow", "SETTINGS"))
        self.Salary_lable.setText(_translate("MainWindow", "Salary"))
        self.Salary_lineEdit.setPlaceholderText(_translate("MainWindow", "Зарплата"))
        self.Pleasure_lable.setText(_translate("MainWindow", "Pleasure"))
        self.Pleasure_lineEdit.setPlaceholderText(_translate("MainWindow", "Развлечения"))
        self.Rest_lable.setText(_translate("MainWindow", "Rest"))
        self.Rest_lineEdit.setPlaceholderText(_translate("MainWindow", "Остальное"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.InfoPleasureLable.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Pleasure costs</span></p>"))
        self.InfoRestLable.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Rest costs</span></p>"))
        self.InfoRemainsLable.setText(_translate("MainWindow", "<p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR </span><span style=\" font-size:18pt;\">Remains</span></p>"))
        self.BackInfoButton.setText(_translate("MainWindow", "BACK"))
        self.coastsPercent.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt;\">0%</span></p></body></html>"))
        self.coastsConLable2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">from </span><span style=\" font-size:16pt; font-weight:600; color:#000000;\">YOUR</span><span style=\" font-size:16pt;\"> salary</span></p></body></html>"))
        self.coastsConLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">YOUR</span><span style=\" font-size:18pt; font-weight:600; color:#67ebff;\"/><span style=\" font-size:18pt;\">costs</span></p></body></html>"))
        self.MoreInfoButton.setText(_translate("MainWindow", "MORE"))
        self.ChangeLabel.setText(_translate("MainWindow", "Change currency"))
        self.CurrencyBox.setItemText(0, _translate("MainWindow", "RUB"))
        self.CurrencyBox.setItemText(1, _translate("MainWindow", "EUR"))
        self.CurrencyBox.setItemText(2, _translate("MainWindow", "USD"))
        self.CurrencyBox.setItemText(3, _translate("MainWindow", "KZT"))
        self.CurrencyBox.setItemText(4, _translate("MainWindow", "UAH"))
        self.CurrencyBox.setItemText(5, _translate("MainWindow", "GBP"))
        self.CurrencyBox.setItemText(6, _translate("MainWindow", "PLN"))
        self.SettingsConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.ClearLOGButton.setText(_translate("MainWindow", "Clear LOG"))
