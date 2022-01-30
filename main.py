import datetime
import json
import os
import subprocess
import sys
import ctypes
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from DialogPy import Dialog
from MainWindow import Ui_ClashForPython
from TrayIconPy import TrayIcon


class MyWindow(QMainWindow, Ui_ClashForPython):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.work = WorkThread()
        self.work.trigger.connect(self.display)
        self.work.start()
        self.Speed = ReflashSpeedThread()
        self.Speed.trigger.connect(self.reflashSpeed)
        self.Speed.start()
        self.setWindowIcon(QIcon('conf/clash-logo.ico'))
        self.setWindowFlags(QtCore.Qt.Window)
        self.ti = TrayIcon(self)
        self.ti.show()
        self.pushButton.clicked.connect(self.btnclick)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, self.tr("提示"),
                                      self.tr("汝妻子我养之，汝勿虑之。\n 汝特么确定要退出吗？"), QtWidgets.QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QtWidgets.QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QtWidgets.QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
            QtWidgets.qApp.quit()
            # sys.exit(app.exec_())
        else:
            event.ignore()
            # 最小化到托盘
            self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
            self.showMinimized()

    def display(self, msg):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        self.listWidget.addItem(msg)

    def reflashSpeed(self, msg):
        self.label_2.setText("上传："+str(round(msg['up'] / (1024 * 1024), 2)) + "MB/s")
        self.label_3.setText("下载："+str(round(msg['down'] / (1024 * 1024), 2)) + "MB/s")

    def btnclick(self):
        print("正在添加按钮")
        self.pushButton2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton2.setGeometry(QtCore.QRect(0, 0, 320, 40))
        self.pushButton2.setMinimumSize(QtCore.QSize(320, 40))
        self.pushButton2.setObjectName("pushButton2")



class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        startCLashService()


class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        url = 'http://localhost:8090/logs'
        r = requests.get(url, stream=True)
        for raw_rsvp in r.iter_lines():
            if raw_rsvp:
                rsvp = json.loads(raw_rsvp)
                self.trigger.emit(str(rsvp.get('payload')))
                print(rsvp)
        print("会执行第二个线程")


class ReflashSpeedThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(dict)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        url = 'http://localhost:8090/traffic'
        r = requests.get(url, stream=True)
        for raw_rsvp in r.iter_lines():
            if raw_rsvp:
                rsvp = json.loads(raw_rsvp)
                self.trigger.emit(dict(rsvp))
                print(rsvp)

def startCLashService():
    config = os.getcwd() + r'\conf\config.yaml'
    cmd = os.getcwd() + r"\core\clash.exe"
    logs = subprocess.run([cmd, "-f", config])


if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("092611")
    app = QApplication(sys.argv)
    myWin = MyWindow()
    thread = Thread()
    thread.start()
    myWin.show()
    sys.exit(app.exec_())
