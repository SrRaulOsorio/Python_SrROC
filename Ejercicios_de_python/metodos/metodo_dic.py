diccionario = {
    "nombre" : "lucas",
    "apellido" : "Dalto",
    "subs" : 100000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() Si no encuentra nada el programa continua
valor_de_kasdks = diccionario.get("jajajaja")
print("hola")

print(claves)

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#Obteniendo un elemento dict-items iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable) 