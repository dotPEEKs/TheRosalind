import sys
import os
from typing import Optional
sys.path.append(os.path.dirname(os.getcwd()))
import PySide6.QtGui
from lib.gui.splash_screen_2 import splas_screen
from PySide6.QtWidgets import QMainWindow,QApplication
from PySide6.QtCore import (
    Qt,
    QTimer)
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
        self.progress_bar_timer.start(1200)
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