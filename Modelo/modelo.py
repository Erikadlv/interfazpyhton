from encodings import utf_8
import pandas as pd
# import sys
# sys.path.append('../Vista')
# from interfaz_ui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

palabra = []

class DataFrame():
    def reading(direccion):
        df = pd.read_csv(direccion,encoding='latin-1')
        df.head()
        print(df)
        for Texto in palabra:
            filtro = df[df['Texto'].str.match(Texto+ r'\b',case=False)]
            print(filtro)
            filtro.to_csv('../prueba.csv', encoding='utf-8' )
            
    def addWord(palabras):
        palabra.append(palabras)
        print(palabra)