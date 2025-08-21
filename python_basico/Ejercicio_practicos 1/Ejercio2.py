#le pedimos al usuario que introdusca una frase o varias.
frase = input("Ingresa una frase y calculamos cuanto tardarias en decirla: ")

#creamos ua lista con todas las palabras de la frase se separan cada vez que haya un espacio.
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos.  
cantidad_de_palabras = len(palabras_separadas)

#condicional para que no escriba una palabara tan larga.
if cantidad_de_palabras > 120:
    print("para, tampoco te pedi un testamento")

#calculamos cuantas palabras dijo y cuanto se tardaria en decirlo.
print(f"Dijiste {cantidad_de_palabras} palabras, tardarias {cantidad_de_palabras/2} segundos en decirla")
print(f"Dalto lo dice en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos")