
#https://unpyside.com/blog/2017/11/21/qtsimpleevent/

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import os


#座標
x, y = -1, -1

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        # .appから実行
        return os.path.join(sys._MEIPASS, relative)
    # 通常実行
    return os.path.join(relative)

def mousePressEvent(e):
    global x,y
    x, y = e.pos().x(), e.pos().y()

def mouseMoveEvent(e):
    global x,y

    if x >= 0 and y >= 0 :
        px, py = e.pos().x(), e.pos().y()
        dlg1.setGeometry(dlg1.pos().x() + (px - x), dlg1.pos().y() + (py - y), dlg1.width(), dlg1.height())

def mouseReleaseEvent(e):
    global x,y
    x, y = -1, -1

def close():
    sys.exit(app.exec())

def expansion():
    if dlg1.isMaximized():
        dlg1.showNormal()
    else:
        dlg1.showMaximized()

def showMinimized():
    dlg1.showMinimized()

app = QtWidgets.QApplication([])
dlg1 = uic.loadUi(f"src\\sigure.ui")

#self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
#self.setAttribute(Qt.WA_TranslucentBackground)  
if __name__ == "__main__":
    dlg1.setWindowFlags(dlg1.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    dlg1.setAttribute(Qt.WA_TranslucentBackground)  
    dlg1.lineEdit.mousePressEvent = mousePressEvent
    dlg1.lineEdit.mouseReleaseEvent = mouseReleaseEvent
    dlg1.lineEdit.mouseMoveEvent = mouseMoveEvent

    dlg1.pushButton_4.setIcon(QIcon(f"images\\close.png"))
    dlg1.pushButton_3.setIcon(QIcon(f"images\\expansion.png"))
    dlg1.pushButton_2.setIcon(QIcon(f"images\\minimize.png"))
    dlg1.pushButton_4.clicked.connect(close)
    dlg1.pushButton_3.clicked.connect(expansion)
    dlg1.pushButton_2.clicked.connect(showMinimized)

    dlg1.show()
    app.exec()
    


    