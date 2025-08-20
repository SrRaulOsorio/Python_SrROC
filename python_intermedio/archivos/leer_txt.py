
#asignando el archivo con una codificacion universal
archivo_sin_leer = open("python_intermedio\\archivos\\prueba_leer_texto.txt", encoding="UTF-8")

#leer archivos completos
#archivo = archivo_sin_leer.read()

#leer linea por linea
lineas = archivo_sin_leer.readlines()

#cerrar el archivo
#archivo.close()


print(lineas)