# -*- coding: utf-8 -*-
import os
import sys

import time
import lackey
from lackey.KeyCodes import Key
import keyboard
from keyboard import mouse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon, QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ctypes import *
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("lol上号器")
        Dialog.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 60, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 110, 231, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 45, 24))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 45, 24))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 20, 231, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 81, 24))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.setPath) #设置
        self.pushButton_2.clicked.connect(self.login) #登录
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "lol登录地址"))
        self.pushButton.setText(_translate("Dialog", "设置"))
        self.pushButton_2.setText(_translate("Dialog", "登录"))
    def setPath(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", ".", '')
        print(directory1)  # 打印文件夹路径
        path = directory1[0]
        self.lineEdit_3.setText(_translate("MainWindow", path))
    def login(self):
        addr= self.lineEdit_3.text()#lol登录程序   一般在tcl文件夹下client.exe
        account= self.lineEdit.text()#登录账号
        password= self.lineEdit_2.text()#登录密码
        if  os.path.exists(addr) and  account !="" and password!="":
            os.system("start  {}".format(addr))
            time.sleep(10)
            lackey.click('photos/123.png')

            # QQ账号
            lackey.click('photos/zhanghao.png')

            time.sleep(1)
            for i in range(15):
                lackey.type(Key.BACKSPACE)
            lackey.type(account)
            time.sleep(0.5)
            lackey.click('photos/mima.png')
            time.sleep(0.5)
            print("Load DD!")
            base_url=os.path.dirname(os.path.realpath(sys.argv[0]))
            driver_url=os.path.join(base_url,r'Drivers\1.Simple\DD94687.64.dll')
            print(driver_url)
            dd_dll = windll.LoadLibrary(driver_url)

            st = dd_dll.DD_btn(0)  # DD Initialize
            if st == 1:
                print("OK")
            else:
                print("Error")
                exit(101)
            # DD虚拟码，可以用DD内置函数转换。DD虚拟键盘
            for i in password:
                dd_dll.DD_str(i)
                time.sleep(0.02)
            time.sleep(0.5)
            # 安全登录
            lackey.click('photos/denglu.png')
            print("登录成功ok")
        else:
            QMessageBox.warning(self, '警告', 'lol地址错误或者账号密码没有填', QMessageBox.Yes)


if __name__ == '__main__':
    # PyQt5高清屏幕自适应设置,以及让添加的高清图标显示清晰，不然designer导入的图标在程序加载时会特别模糊
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)
    font = QFont('Microsoft YaHei')
    font.setPixelSize(11)
    app.setFont(font)
    MainWindow = QMainWindow()
    interface = Ui_Dialog()
    interface.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())