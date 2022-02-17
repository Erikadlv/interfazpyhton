import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('palabrasfiltradas.csv', index_col=0,encoding='latin-1') 
a = list(df['Texto']) 
texto = ' '.join(str(e) for e in a) 