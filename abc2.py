import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import *


class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1918, 1028)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 101))
        self.label_2.setStyleSheet("background-image:url(c:/Users/pc/Desktop/inpt/pfa/Capture.PNG);\n"
"")

        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:/Users/pc/Desktop/inpt/pfa/Capture.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 20, 103, 49))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("\n"
"\n"
"color: rgb(150, 192, 179);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("\n"
"color: rgb(150, 192, 179);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)


        self.pushButton_2.setGeometry(QtCore.QRect(900, 430, 121, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(150, 192, 179);color:rgb(11, 11, 11);font: 81 8pt Rockwell Extra Bold;border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.getImage)
        self.pushButton.clicked.connect(self.show_new_window)
        self.pushButton.setGeometry(QtCore.QRect(900, 370, 121, 51))
        self.pushButton.setStyleSheet("background-color: rgb(150, 192, 179);color:rgb(11, 11, 11);font: 81 8pt Rockwell Extra Bold;border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1050, 430, 61, 41))

        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("c:/Users/pc/Desktop/inpt/pfa/play1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(810, 430, 61, 41))
        self.label_10.setStyleSheet("background-image:url(c:/Users/pc/Desktop/inpt/pfa/play.png);")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("c:/Users/pc/Desktop/inpt/pfa/play.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(620, 490, 711, 501))

        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(-10, 10, 16, 1051))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 70, 1571, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(141, 0))
        self.label.setMaximumSize(QtCore.QSize(141, 16777215))
        self.label.setStyleSheet("border-radius:10px ;color:rgb(11, 11, 11); background-color: rgb(150, 192, 179);font: 75 8pt MS Shell Dlg 2;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(141, 0))
        self.label_8.setMaximumSize(QtCore.QSize(141, 16777215))
        self.label_8.setStyleSheet("color:rgb(11, 11, 11);background-color: rgb(150, 192, 179);font: 75 8pt MS Shell Dlg 2;border-radius :10px;")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(141, 0))
        self.label_5.setMaximumSize(QtCore.QSize(141, 16777215))
        self.label_5.setStyleSheet("color:rgb(11, 11, 11);border-radius :10px ; background-color: rgb(150, 192, 179);font: 75 8pt MS Shell Dlg 2;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.hide
        self.pushButton_4.hide

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "ABULLCASSIS"))
        self.label_7.setText(_translate("MainWindow", "DR-AI"))
        self.pushButton_2.setText(_translate("MainWindow", "parcourire"))
        self.pushButton.setText(_translate("MainWindow", "valider"))

        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "  Nom du pacient "))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "          Date    "))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "     commentaire"))



    def getImage(self):
        print("hi")
        _translate = QtCore.QCoreApplication.translate
        print("hi")
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:/Users/pc/Desktop/inpt/pfa', "Image files (*.jpg *.gif)")
        self.imagePath = fname[0]
        self.pixmap1 = QtGui.QPixmap(self.imagePath)

        self.label_11.setPixmap(QtGui.QPixmap(self.pixmap1))
        self.label_11.setScaledContents(True)

        self.pushButton_3.setGeometry(QtCore.QRect(330, 700, 171, 81))
        self.pushButton_3.setStyleSheet("background-color: rgb(150, 192, 179);\n"
"color:rgb(11, 11, 11);\n"
"font: 81 8pt \"Rockwell Extra Bold\";\n"
"border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4.setGeometry(QtCore.QRect(1470, 710, 151, 81))
        self.pushButton_4.setStyleSheet("background-color: rgb(150, 192, 179);\n"
"color:rgb(11, 11, 11);\n"
"font: 81 8pt \"Rockwell Extra Bold\";\n"
"border-radius:10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.setText(_translate("MainWindow", "segmentation"))
        self.pushButton_4.setText(_translate("MainWindow", "detection"))

    def show_new_window(self):
            w.show()




if __name__=="_main_":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    w=AnotherWindow()
    sys.exit(app.exec_())
