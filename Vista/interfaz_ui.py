# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 384)
        font = QtGui.QFont()
        font.setFamily("FiraCode NF")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget\n"
"{\n"
"background: #FFF8DC;\n"
"}\n"
"QFrame{\n"
"background: #FFDEAD;\n"
"}\n"
"QPushButton{\n"
"background: #1E90FF;\n"
"color: #fff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit{\n"
"border-radius:20px;\n"
"color: #0000FF\n"
"}\n"
"QLabel{\n"
"color: #0000FF\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 241, 31))
        font = QtGui.QFont()
        font.setFamily("FiraCode NF")
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 260, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 491, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 130, 81, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 130, 141, 21))
        font = QtGui.QFont()
        font.setFamily("FiraCode NF")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))
        self.menubar.setObjectName("menubar")
        self.menuARchivo = QtWidgets.QMenu(self.menubar)
        self.menuARchivo.setObjectName("menuARchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuARchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programa Python 1"))
        self.pushButton.setText(_translate("MainWindow", "Cargar Archivo"))
        self.pushButton_2.setText(_translate("MainWindow", "Guardar Archivo"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Escriba la plabra clave"))
        self.pushButton_4.setText(_translate("MainWindow", "Nube de Palabras"))
        self.pushButton_5.setText(_translate("MainWindow", "Histograma"))
        self.label_2.setText(_translate("MainWindow", "Menú base de datos reducida"))
        self.pushButton_3.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Palabra Clave:"))
        self.menuARchivo.setTitle(_translate("MainWindow", "Archivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

