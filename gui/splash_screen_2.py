# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recreated.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)
from PySide6.QtCore import QTimer
class splas_screen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 739)
        MainWindow.setStyleSheet(u"QLabel#watermark {\n"
"	background-color: rgb(255, 174, 205);\n"
"	color: rgb(255, 249, 251);\n"
"	font: 75 16pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#circle_frame {\n"
"	border-image: url(\"fixed.jpg\");\n"
"}\n"
"\n"
"QFrame#frame_5 {\n"
"	background-color: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel#welcome_watermark {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Unispace\";\n"
"}\n"
"\n"
"QProgressBar {\n"
"	background: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 0, 214, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QLabel#label_of_progress_bar {\n"
"	font: 75 12pt \"Unispace\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel#logon_page_main_text {\n"
"	font: 75 12pt \"Unispace\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel#author_text {\n"
"	font: 75 12pt \"Unispace\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	\n"
"	\n"
"\n"
"	\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(280, 130, 341, 321))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 20, 30, 20)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.circle_frame = QLabel(self.frame_3)
        self.circle_frame.setObjectName(u"circle_frame")

        self.verticalLayout_3.addWidget(self.circle_frame)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(280, 40, 341, 81))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.welcome_watermark = QLabel(self.frame_5)
        self.welcome_watermark.setObjectName(u"welcome_watermark")
        self.welcome_watermark.setGeometry(QRect(90, 20, 121, 20))
        self.welcome_watermark.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(250, 510, 641, 101))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_of_progress_bar = QLabel(self.frame_6)
        self.label_of_progress_bar.setObjectName(u"label_of_progress_bar")
        self.label_of_progress_bar.setGeometry(QRect(90, 70, 471, 20))
        self.logon_page_main_text = QLabel(self.frame_6)
        self.logon_page_main_text.setObjectName(u"logon_page_main_text")
        self.logon_page_main_text.setGeometry(QRect(20, 50, 461, 20))
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(170, 440, 641, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.progress_bar = QProgressBar(self.frame_7)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(140, 30, 291, 21))
        self.progress_bar.setMinimum(2)
        self.progress_bar.setValue(10)
        self.frame_author = QFrame(self.centralwidget)
        self.frame_author.setObjectName(u"frame_author")
        self.frame_author.setGeometry(QRect(280, 580, 351, 80))
        self.frame_author.setFrameShape(QFrame.StyledPanel)
        self.frame_author.setFrameShadow(QFrame.Raised)
        self.author_text = QLabel(self.frame_author)
        self.author_text.setObjectName(u"author_text")
        self.author_text.setGeometry(QRect(20, 40, 351, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.circle_frame.setText("")
        self.welcome_watermark.setText(QCoreApplication.translate("MainWindow", u"The Rosalind", None))
        self.label_of_progress_bar.setText("")
        self.logon_page_main_text.setText(QCoreApplication.translate("MainWindow", u"THE ROSALIND OTOMATIK \u0130NSTAGRAM DM BOTU", None))
        self.progress_bar.setFormat("")
        self.author_text.setText(QCoreApplication.translate("MainWindow", u"Coded & Designed By Alperen \u00c7avu\u015f", None))
    # retranslateUi

class Main(QMainWindow,splas_screen):
    def __init__(self,parent):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.progress_bar_timer = QTimer()
        self.progress_bar_timer.timeout.connect(self.increase_progress_bar)
        self.progress_bar_counter = 2
        self._parent = parent
        self.progress_bar_timer.start(25)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
    def increase_progress_bar(self):
        current_val = self.progress_bar.value()
        self.progress_bar_counter = self.progress_bar_counter + 1
        if self.progress_bar_counter >= self.progress_bar.maximum():
            self.progress_bar_timer.stop()
            self.close()
            self._parent.show()
        else:
            self.progress_bar.setValue(self.progress_bar_counter)