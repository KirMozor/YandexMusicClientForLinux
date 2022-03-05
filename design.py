# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Svg/icon_main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonToDownload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonToDownload.setObjectName("pushButtonToDownload")
        self.horizontalLayout.addWidget(self.pushButtonToDownload)
        self.writeLinkToPlay = QtWidgets.QLineEdit(self.centralwidget)
        self.writeLinkToPlay.setObjectName("writeLinkToPlay")
        self.horizontalLayout.addWidget(self.writeLinkToPlay)
        self.pushButtonToPlay = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonToPlay.setObjectName("pushButtonToPlay")
        self.horizontalLayout.addWidget(self.pushButtonToPlay)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YandexMusic Client"))
        self.pushButtonToDownload.setText(_translate("MainWindow", "Скачать"))
        self.writeLinkToPlay.setText(_translate("MainWindow", "Введи ссылку на трек"))
        self.pushButtonToPlay.setText(_translate("MainWindow", "Играть трек"))
