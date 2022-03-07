# interfazpython

## Escoge un tema para analizar tweets (BaseDatos.csv) focaliza sus palabras clave
  
- Elabora una Interfaz gráfica (GUI) en Python.

- La interfaz será de diseño libre

## Menú Base de datos reducida

- En esta primera etapa contendrá un menú para "Crear base de datos reducida".

- Deberá tener un mecanismo para ingresar las palabras claves que queremos buscar en la base de datos.

- En este menú se deberá tener la opción para leer un archivo csv. El mecanismo para seleccionar el archivo será un file chooser.

- Recorrerá la base de datos en busca de los registros que contengan las palabras claves y las copiara en nuevo archivo.

- Deberá proporcionar un mecanismo para (Save File) para guardar el nuevo archivo generado.

> OJO: Debes usar MVC y el código de la lógica de negocios debe estar en
> POO.

## Menú Frecuencia de Palabras

- Opción "Nube de palabras":

- Usando la librería WordCloud de Python

- Lee el archivo CSV y Genera una nube de palabras, no te olvides de configurar los "StopWords"

- Opción "Histograma":

- Usando una librería gráfica Matplotlib, Bokeh, Seaborn crea un histograma de las frecuencia de palabras que más aparecen en la base de datos reducida, no te olvides de los stop words.

> OJO: Debes usar MVC y el código de la lógica de negocios debe estar en
> POO.


- Red neuronal:
Adapta el ejemplo de red neuronal proporcionado para que funcione con POO
La red neuronal debe leer un csv que será el training set y entrenar la red


- Menú red neuronal:
Debe dar la opción para leer un training set (csv) que servirá para entrenar la red neuronal, debe avisar que el procedimiento de entrenamiento a terminado
Debe dar la opción  de poder introducir una pregunta a red neuronal, sobre nuevas situaciones y dar respuesta a esta pregunta