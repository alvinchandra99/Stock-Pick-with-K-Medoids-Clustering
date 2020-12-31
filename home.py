# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import cluster


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 473)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 71, 31))
        self.pushButton.setStyleSheet(
            "font: 87 8pt \"Century Gothic\";background-color: rgb(185, 239, 255);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 50, 281, 61))
        self.label.setAcceptDrops(True)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 87 24pt \"Century Gothic\";")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 220, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(60, 280, 311, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(60, 340, 311, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(140, 230, 20, 181))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(60, 400, 311, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(50, 230, 20, 181))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(360, 230, 20, 181))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 71, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 300, 71, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 71, 31))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 240, 191, 31))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(
            "font: 8pt \"Century Gothic\";background-color: rgb(136, 255, 85)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 300, 191, 31))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(
            "font: 8pt \"Century Gothic\";background-color: rgb(136, 255, 85)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 360, 191, 31))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(
            "font: 8pt \"Century Gothic\";background-color: rgb(136, 255, 85)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 180, 531, 31))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("font: 87 8pt \"Century Gothic\";")
        self.label_8.setAlignment(QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 80, 111, 61))
        self.pushButton_2.setStyleSheet(
            "font: 87 8pt \"Century Gothic\";background-color: rgb(185, 239, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 170, 111, 61))
        self.pushButton_3.setStyleSheet(
            "font: 87 8pt \"Century Gothic\";background-color: rgb(185, 239, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 260, 111, 61))
        self.pushButton_4.setStyleSheet(
            "font: 87 8pt \"Century Gothic\";background-color: rgb(185, 239, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 350, 111, 61))
        self.pushButton_5.setStyleSheet(
            "font: 87 8pt \"Century Gothic\";background-color: rgb(185, 239, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.label.setText(_translate("MainWindow", "Stock Data"))
        self.label_2.setText(_translate("MainWindow", "Market Cap"))
        self.label_3.setText(_translate("MainWindow", "PE"))
        self.label_4.setText(_translate("MainWindow", "Beta"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "-"))
        self.pushButton_2.setText(_translate("MainWindow", "Cluster Stock"))
        self.pushButton_3.setText(_translate("MainWindow", "About"))
        self.pushButton_4.setText(_translate("MainWindow", "Guide"))
        self.pushButton_5.setText(_translate("MainWindow", "Update"))

        self.pushButton.clicked.connect(self.show)
        self.pushButton_2.clicked.connect(self.showCluster)
        self.pushButton_5.clicked.connect(self.validationUpdate)
        self.pushButton_3.clicked.connect(self.showAbout)
        self.pushButton_4.clicked.connect(self.showGuide)

    def market_cap(self):
        df = pd.read_excel('DataSaham5.xlsx',
                           sheet_name='Sheet1')
        kode_saham = self.lineEdit.text().upper()
        market_cap = str(
            (df.loc[df['kode_saham'] == kode_saham]['Market_Cap'].values[0])/1000000000) + ' T '
        return market_cap

    def PE(self):
        df = pd.read_excel('DataSaham5.xlsx',
                           sheet_name='Sheet1')
        kode_saham = self.lineEdit.text().upper()
        PE = str(df.loc[df['kode_saham'] == kode_saham]['PE'].values[0])
        isNegative = str(
            df.loc[df['kode_saham'] == kode_saham]['Negative PE'].values[0])
        if(isNegative == 'N'):
            return PE
        if(isNegative == 'Y'):
            return PE + ' (laba rugi)'

    def beta(self):
        df = pd.read_excel('DataSaham5.xlsx',
                           sheet_name='Sheet1')
        kode_saham = self.lineEdit.text().upper()
        beta = str(df.loc[df['kode_saham'] == kode_saham]['Beta_x'].values[0])
        return beta

    def nama(self):
        df = pd.read_excel('namaperusahaan.xlsx',
                           sheet_name='Sheet1')
        kode_saham = self.lineEdit.text().upper()
        nama = str(df.loc[df['kode_saham'] == kode_saham]['Nama'].values[0])
        return nama

    def show(self):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        try:
            self.label_5.setText(_translate("MainWindow", self.market_cap()))
            self.label_6.setText(_translate("MainWindow", self.PE()))
            self.label_7.setText(_translate("MainWindow", self.beta()))
            self.label_8.setText(_translate("MainWindow", self.nama()))

        except:
            msg = QMessageBox()
            msg.setText('Kode Saham Tidak Ditemukan!')
            msg.exec_()

    def showAbout(self):
        import about
        self.windowAbout = QtWidgets.QMainWindow()
        self.uiAbout = about.Ui_MainWindow()
        self.uiAbout.setupUi(self.windowAbout)
        self.windowAbout.show()

    def showGuide(self):
        import guide
        self.windowGuide = QtWidgets.QMainWindow()
        self.uiGuide = guide.Ui_MainWindow()
        self.uiGuide.setupUi(self.windowGuide)
        self.windowGuide.show()

    def showCluster(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = cluster.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def validationUpdate(self):
        self.update()

    def update(self):
      #  try:

        import update

        self.windowUpdate = QtWidgets.QMainWindow()
        self.uiUpdate = update.Ui_MainWindow()
        self.uiUpdate.setupUi(self.windowUpdate)
        self.windowUpdate.show()


       # except:
        #    msg = QMessageBox()
        #   msg.setText('Tidak dapat terhubung ke Internet')
        #  msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
