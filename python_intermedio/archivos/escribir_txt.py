with open("python_intermedio\\archivos\\prueba_leer_texto.txt", "w", encoding="UTF-8") as archivos:
    #sobre escribimos el archivo
    #archivos.write("jajajajaj te la recontra tecleeeee")
    #archivos.write("prueba prueba prueba")
    
    #agregando lineas con writelines
    archivos.writelines(["- Hola maestrocomo estas?\n", "- misericordia\n"])
    
    #agregando mas lineas
    archivos.writelines(["- No se porque disjiste eso\n", "- yo tampoco se\n"])
    