#creando diccionario con dict()
diccionario = dict(npmbre="ruben", apellido="aguirre")

#las listas no pueden ser claves si se utiliza frozenset para meter conjuntos
diccionario = {frozenset(["dato1","dato2"]):"dato3"}

#creando siccionario con fromkeys con dos parametros
diccionario = dict.fromkeys(["dato1","dato2"],"dato3")

#creando siccionario con fromkeys con dos parametros con un valor modificado
diccionario = dict.fromkeys(["dato1","dato2","dato3"])

print(diccionario)
print(diccionario["dato3"])