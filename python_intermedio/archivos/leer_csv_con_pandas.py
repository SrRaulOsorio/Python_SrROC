import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#archivos = pd.read_csv("python_intermedio\\archivos\\datos.csv")

#obteniendo todos los datos
#print(archivos)

#data frame 
df = pd.read_csv("python_intermedio\\archivos\\datos.csv")#,names=["name","lastname","age"])  (Lo podemos usar como referencia)
df2 = pd.read_csv("python_intermedio\\archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenandolos por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

#concatenando a las dos dataframe
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras filas con head()
primeras_filas = df.head(1)

#accediendo a las ultimas filastail()
ultimas_filas = df.tail(1)

#accediendo a la cantidad de filas y columnas shape
#filas_y_columnas_totales = df.shape
filas_totales,columna_totales = df.shape

#existe la posibilidad de acceder a cualquier posicion de la tabla dependiendo lo que necesitemos
#solo que en este momento no es necesario para lo que vamos a realizar en el proyecto

#slicing
#cadena = "0123456789"
#print(cadena)

#mostrar los datos
#print(df)
#print(df_concatenado)
#print(primeras_filas)
#print(ultimas_filas)
#print(filas_y_columnas_totales)
print(columna_totales)
print(filas_totales)