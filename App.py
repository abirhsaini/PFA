from cProfile import label
from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface1 import Ui
from interface0 import Ui_MainWindow
from interface2 import Ui_MainWindow2
from petitWindow import AnotherWindow
import sys
import os

##from abc1 import Ui_MainWindow2 as aaa


def Navigate():
    widget.setCurrentIndex(widget.currentIndex()+1)
    interface2.line.setText(interface1.line.text())
    interface2.line1.setDate(interface1.line1.date())
    interface2.line2.setText(interface1.line2.text())
    print(interface2.line.text())
    interface3.line.setText(interface2.line.text())
    interface3.line1.setDate(interface2.line1.date())
    interface3.line4.setText(interface2.line2.text())
    

def show_new_window(self):
    ui2.show()    

def Valider(self):
    if (interface3.line.text()=="") or (interface3.line1.date()=="PyQt5.QtCore.QDate(2000, 1, 1)"):
        interface3.titre4.show()
    else:
        interface3.titre1.show()    
        


def enregistrer():
    
        
        
        try:
            os.mkdir("c:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/"+interface3.line.text()+" "+ str(interface3.line1.date().day())+"-"+str(interface3.line1.date().month())+"-"+str(interface3.line1.date().year()))
            fichier = open("c:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/"+interface3.line.text()+" "+ str(interface3.line1.date().day())+"-"+str(interface3.line1.date().month())+"-"+str(interface3.line1.date().year())+"/Synthèse.txt", "a+")
            fichier.write("nom: "+ interface3.line.text()+"\n"+"date: "+ interface3.line1.text() + "\n"+ "commentaire: " +interface3.line4.text())
            fichier.close()
            interface3.titre2.show()
        except:
            interface3.titre3.show()

    
def Navigate1():
    widget.setCurrentIndex(widget.currentIndex()-1)
    interface1.line.setText(interface2.line.text())
    interface1.line1.setDate(interface2.line1.date())
    interface1.line2.setText(interface2.line2.text())
    interface2.line.setText(interface3.line.text())
    interface2.line1.setDate(interface3.line1.date())
    interface2.line2.setText(interface3.line4.text())
    
    


app=QApplication(sys.argv)
Window=QtWidgets.QMainWindow()
widget=QtWidgets.QStackedWidget()
widget.setWindowIcon(QtGui.QIcon("PFA2.png"))
widget.setWindowTitle("PFA")
widget.setStyleSheet("background-color: #FFFFFF")

interface1=Ui_MainWindow()
interface1.setupUi(Window)
interface1.valider.clicked.connect(Navigate)


interface2=Ui()
Window1=QtWidgets.QMainWindow()
interface2.setupUi(Window1)
interface2.photo7.clicked.connect(Navigate1)



interface3=Ui_MainWindow2()
Window2=QtWidgets.QMainWindow()
interface3.setupUi(Window2)
interface3.label.clicked.connect(show_new_window)
interface3.titre1.clicked.connect(enregistrer)
interface3.photo7.clicked.connect(Navigate1)
interface2.Segmentation.clicked.connect(Navigate)
interface2.Detection.clicked.connect(Navigate)
interface3.btn5.clicked.connect(Valider)


ui2=AnotherWindow()
##sc2=aa
##sc3=aaa
widget.addWidget(Window)
widget.addWidget(Window1)
widget.addWidget(Window2)
##widget.addWidget(sc2)
##widget.addWidget(sc3)
widget.resize(1920,1080)
widget.show()
sys.exit(app.exec_())







