# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_main_dialog(object):
    def setupUi(self, main_dialog):
        if not main_dialog.objectName():
            main_dialog.setObjectName(u"main_dialog")
        main_dialog.resize(440, 440)
        main_dialog.setMinimumSize(QSize(440, 440))
        main_dialog.setMaximumSize(QSize(440, 440))
        icon = QIcon()
        icon.addFile(u":/resource/main_window.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_dialog.setWindowIcon(icon)
        main_dialog.setStyleSheet(u"QLineEdit#username {\n"
"	font: 75 8pt \"Unispace\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit#password {\n"
"	font: 75 8pt \"Unispace\";\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#login_button {\n"
"	font: 75 8pt \"Unispace\";\n"
"	background-color: rgb(255, 119, 249);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#user_logon_app_name_label_text {\n"
"	font: 75 20pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#user_logon_app_description_label_text {\n"
"	font: 75 20pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#login_author_label_text {\n"
"	font: 75 9pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#user_eula_text {\n"
"	font: 75 9pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#login_author_label_text {\n"
"	font: 75 8pt \"Unispace\";\n"
"}\n"
"\n"
"QLabel#login_auth_text {\n"
"	font: 75 8pt \"Unispace\";\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 224, 254);\n"
"}\n"
"\n"
"\n"
"	")
        self.main_bg_label = QLabel(main_dialog)
        self.main_bg_label.setObjectName(u"main_bg_label")
        self.main_bg_label.setGeometry(QRect(-210, -30, 871, 681))
        self.main_bg_label.setStyleSheet(u"")
        self.main_bg_label.setPixmap(QPixmap(u":/resource/assets/images/main_bg.jpg"))
        self.user_logon_icon_label = QLabel(main_dialog)
        self.user_logon_icon_label.setObjectName(u"user_logon_icon_label")
        self.user_logon_icon_label.setGeometry(QRect(190, 130, 61, 101))
        self.user_logon_icon_label.setPixmap(QPixmap(u"main_window.ico"))
        self.user_logon_app_name_label_text = QLabel(main_dialog)
        self.user_logon_app_name_label_text.setObjectName(u"user_logon_app_name_label_text")
        self.user_logon_app_name_label_text.setGeometry(QRect(130, 60, 261, 41))
        self.user_logon_app_name_label_text.setStyleSheet(u"")
        self.username = QLineEdit(main_dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 240, 241, 31))
        self.password = QLineEdit(main_dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 280, 241, 31))
        self.password.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton(main_dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(170, 370, 75, 23))
        self.user_logon_app_description_label_text = QLabel(main_dialog)
        self.user_logon_app_description_label_text.setObjectName(u"user_logon_app_description_label_text")
        self.user_logon_app_description_label_text.setGeometry(QRect(100, 110, 381, 41))
        self.login_author_label_text = QLabel(main_dialog)
        self.login_author_label_text.setObjectName(u"login_author_label_text")
        self.login_author_label_text.setGeometry(QRect(140, 420, 181, 21))
        self.login_auth_text = QLabel(main_dialog)
        self.login_auth_text.setObjectName(u"login_auth_text")
        self.login_auth_text.setGeometry(QRect(100, 320, 231, 41))

        self.retranslateUi(main_dialog)

        QMetaObject.connectSlotsByName(main_dialog)
    # setupUi

    def retranslateUi(self, main_dialog):
        main_dialog.setWindowTitle(QCoreApplication.translate("main_dialog", u"THE ROSALIND ", None))
        self.main_bg_label.setText("")
        self.user_logon_icon_label.setText("")
        self.user_logon_app_name_label_text.setText(QCoreApplication.translate("main_dialog", u"THE ROSALIND", None))
        self.username.setPlaceholderText(QCoreApplication.translate("main_dialog", u"Kullan\u0131c\u0131 Adi Girin", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("main_dialog", u"\u015eifre Girin", None))
        self.login_button.setText(QCoreApplication.translate("main_dialog", u"Giri\u015f", None))
        self.user_logon_app_description_label_text.setText(QCoreApplication.translate("main_dialog", u"INSTAGRAM DM BOT", None))
        self.login_author_label_text.setText(QCoreApplication.translate("main_dialog", u"Coded By Alperen", None))
        self.login_auth_text.setText("")
    # retranslateUi

