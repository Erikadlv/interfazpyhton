import sys
sys.path.append('../Vista')
sys.path.append('../Modelo')
from interfaz_ui import *
from modelo import *
from histograma import *
from cloud import *
from red import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFileNameDialog)
        # self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.words)
        self.pushButton_3.clicked.connect(self.palabra)
        self.pushButton_4.clicked.connect(self.nub)
        self.pushButton_5.clicked.connect(self.ghisto)
        self.pushButton_6.clicked.connect(self.Network)
        
    
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.lineEdit.setText(fileName)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            
    def words(self):
        direccion = self.lineEdit.text()
        DataFrame.reading(direccion)

    def ghisto(self):
        direccion = self.lineEdit.text()
        Histo.Histograma(direccion)
    
    def palabra(self):
        palabras = self.lineEdit_2.text()
        DataFrame.addWord(palabras)
        self.lineEdit_2.setText('')
        
    def nub(self):
        direccion = self.lineEdit.text()
        nube.cloudWord(direccion)

    def Network(self):
        NeuralNetwork.init(self)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()