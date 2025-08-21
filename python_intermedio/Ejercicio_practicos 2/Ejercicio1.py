#falto el profe y los pibes van a armar la clase

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando con un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun la redad
    compañeros.sort(key=lambda x :x[1])
    
    #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desmpaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(3)

#mostramos el resultado
print(f"El profesor es: {profesor} y su aistente es: {asistente}")