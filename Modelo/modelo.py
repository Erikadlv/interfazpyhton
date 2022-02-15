import pandas as pd
# import sys
# sys.path.append('../Vista')
# from interfaz_ui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class DataFrame():
    def reading(direccion):
        df = pd.read_csv(direccion, header=None,encoding='latin-1')
        # df.head()
        print(df)