with open("python_intermedio\\archivos\\prueba_leer_texto.txt", "a", encoding="UTF-8") as archivos:
    #agregando 
    #archivos.write("jajajajaja te la recontra tecleeee \n")
    
    #bucle para agregar varias lineas 
    archivos.write("\n")
    for i in range(5):
        #agregando lineas
        archivos.write(f"linea {i+1} agregada\n")