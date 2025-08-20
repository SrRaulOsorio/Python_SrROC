import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#archivos = pd.read_csv("python_intermedio\\archivos\\datos.csv")

#obteniendo todos los datos
#print(archivos)

#data frame 
df = pd.read_csv("python_intermedio\\archivos\\datos.csv")#,names=["name","lastname","age"])  (Lo podemos usar como referencia)

#obteniendo los datos de la columna nombre
nombres = df["name"]

#mostrar los datos
print(df)11