#abriendo el archivo con with open
with open("python_intermedio\\archivos\\prueba_leer_texto.txt", encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(archivo.read())
    
#no es necesario cerrerlo al usar with open