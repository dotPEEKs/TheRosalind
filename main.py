#Main login page dialog
import sys
import time
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QDialog,QApplication,QMainWindow
from PySide6.QtCore import Qt
from lib.gui.login_model_1 import Ui_main_dialog
from lib.security.hashing import HMAC
from lib.gui.main_model_2 import Ui_MainWindow
from lib.gui.splash_screen_2 import Main,splas_screen
from win10toast import ToastNotifier
class MainScreen(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

class splashScreen(QMainWindow,splas_screen):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

class LoginModel(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_main_dialog()
        self.ui.setupUi(self)
        self.key = b"\xec\x9d\x02b\xd2\x9e\xc1\xe1\x12?\xd4\xe99(\x9bF\x92\xa6\x03\x12^%\xee\xc9\xec\xf8\xb9'\x83Fw\x1c"
        self.real_pwd = b"\x1c\xe5\xab\xa7\xcd\xbb\x9fF_\xe5Au\x16\xdd2M\x08\xb2\xd2\x1a\x89I\x1f\x8f\xbd\x81\xa8\xf7\x10wA'"
        self.real_username = b"\x1c\xe5\xab\xa7\xcd\xbb\x9fF_\xe5Au\x16\xdd2M\x08\xb2\xd2\x1a\x89I\x1f\x8f\xbd\x81\xa8\xf7\x10wA'"
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.hmac = HMAC()
        self.hmac.key = self.key
        self.ui.login_button.clicked.connect(self.validate_credential)
        self.limit = 0
        self.notification_toaster = ToastNotifier()
    def validate_credential(self) -> bool:
        username = self.ui.username.text().encode()
        passwd = self.ui.password.text().encode()
        if self.limit == 3:
            self.ui.login_auth_text.setText("Uygulama kilitlenmiştir.\nMail Kutunuza gelen kodu girerek\ntekrardan giriş yapabilirsiniz")
        elif len(username) == 0:
            self.ui.login_auth_text.setText("Yetersiz kullanıcı adı uzunluğu")
        elif len(passwd) == 0:
            self.ui.login_auth_text.setText("Yetersiz Şifre Uzunluğu")
        elif not self.validate_user_name(username):
            self.limit = self.limit + 1
            self.ui.login_auth_text.setText("Geçersiz kullanıcı adı \nKalan giriş hakkınız : %s/3" % (self.limit))
        elif not self.validate_pwd(passwd):
            self.limit = self.limit + 1
            self.ui.login_auth_text.setText("Geçersiz Şifre \nKalan giriş hakkınız : %s/3" % (self.limit))
        else:
            self.ui.login_auth_text.setText("Giriş yapılıyor ....")
            self.notification_toaster.show_toast(title="Bildiri",
                msg = "\nGiriş Yapıldı %s" % (time.strftime("%H:%M %d.%m.%Y")),
                icon_path=".\\main_window.ico",
                threaded=True
            )
            self.accept()
    def validate_user_name(self,user_input) -> bool:
        self.hmac.msg = user_input
        if self.hmac.out == self.real_username:
            return True
        return False
    def validate_pwd(self,user_input):
        self.hmac.msg = user_input
        if self.hmac.out == self.real_pwd:
            return True
        return False
    
application = QApplication(sys.argv)
window = LoginModel()
window.setModal(False)
_parent = MainScreen()
if window.exec():
    window.close()
    main_window = Main(parent=_parent)
    main_window.show()
sys.exit(application.exec())
