from PyQt5 import QtWidgets, QtCore

from siderbotton import MainWindow


class Dialog(QtWidgets.QMainWindow):
    def __init__(self, MainWindow, parent=None):
        super(Dialog, self).__init__(parent)

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
            MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
            MainWindow.showMinimized()

        # 默认直接调用QMessageBox.question 弹出询问的方法
        # reply = QtWidgets.QMessageBox.question(self,
        #                                        '本程序',
        #                                        "是否要退出程序？",
        #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        # if reply == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # elif reply == QtWidgets.QMessageBox.No:
        #     event.ignore()
        #     MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        #     MainWindow.showMinimized()
        # else:
        #     # 最小化到托盘
        #     MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        #     MainWindow.showMinimized()