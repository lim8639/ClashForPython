import json
import os
import subprocess
import sys

import requests
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_ClashForPython


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

    def display(self, msg):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        # self.listWidget.addItem(msg)
        print(msg)

    def reflashSpeed(self, msg):
        # self.label_2.setText(str(round(msg['up'] / (1024 * 1024), 2)) + "MB/s")
        # self.label_5.setText(str(round(msg['down'] / (1024 * 1024), 2)) + "MB/s")
        print(msg)


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


def startCLashService():
    config = os.getcwd() + r'\conf\config.yaml'
    cmd = os.getcwd() + r"\core\clash.exe"
    logs = subprocess.run([cmd, "-f", config])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    thread = Thread()
    thread.start()
    myWin.show()
    sys.exit(app.exec_())
