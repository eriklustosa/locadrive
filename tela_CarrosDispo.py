# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_CarrosDispo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class OP_CarDispo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 861, 151))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(230, 70, 321, 61))
        self.widget_3.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(20, 10, 281, 41))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(70, 3, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(17)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(260, -10, 261, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("carro.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"background-color: rgb(189, 189, 189);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 270, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 270, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 550, 75, 23))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"background-color: rgb(189, 189, 189);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(-20, 480, 811, 21))
        self.widget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 240, 811, 21))
        self.widget_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_5.setObjectName("widget_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 360, 161, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMAGEM_SUV.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 350, 221, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("CARRO_PICAPES.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 360, 181, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("CARRO_SEDAN.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 160, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "Carros Disponiveis"))
        self.pushButton.setText(_translate("MainWindow", "Categoria (A) SUV"))
        self.pushButton_2.setText(_translate("MainWindow", "Categoria (B) Picapes "))
        self.pushButton_3.setText(_translate("MainWindow", "Categoria (C) Sedan"))
        self.pushButton_4.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Busque por Uma Categoria de Carros que Deseja Alugar!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = OP_CarDispo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())