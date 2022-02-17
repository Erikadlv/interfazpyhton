import pandas as pd
import matplotlib.pyplot as plt


class Histo():
    def Histograma(direccion):  
        df = pd.read_csv(direccion, index_col=0,encoding='latin-1') 
        a = list(df['Texto']) 
        texto = ' '.join(str(e) for e in a) 
        quitar = ",;:.\n!\"'"
        for caracter in quitar:
            texto = texto.replace(caracter,
                                "")  # Remplazarlo por "nada"; es decir, removerlo
        # Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
        texto = texto.lower()
        # Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
        palabras = texto.split(" ")
        # Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
        # será la palabra, y el valor será el conteo
        diccionario_frecuencias = {}
        for palabra in palabras:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            else:
                diccionario_frecuencias[palabra] = 1

        for palabra in diccionario_frecuencias:
            frecuencia = diccionario_frecuencias[palabra]
            print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")

        data = palabras

        n, bins, patches=plt.hist(data)
        plt.xlabel("Palabras")
        plt.ylabel("Frecuencia")
        plt.title("Histograma")
        plt.show()
