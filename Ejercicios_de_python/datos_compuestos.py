#Una lista puede modificar
lista = ["Limon", "Granja", True,1.70]

#Una tupla no puede modificar 
tupla = {"Limon", "Granja", True, 1.70}

#esto es valido
lista[3] = "Maquinola" 

#Esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set)
conjunto = {"Limon", "Granja", True, 1.70}
#Los conjuntos no tienen indice
#conjunto[3] = "Maquinola" #No es valido
#print(conjunto)
#el conjunto no admite repetidos

#creando un diccionario (dict)
diccionario = {
    "nombre": "Limon",
    "tipo": "Fruta",
    "cantidad": 5,
    "precio": 1.50
}

print(diccionario["nombre"]) #Accediendo a un valor del diccionario