#creando una lista con list
lista = list([100])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
agregando_elemento = lista.append(100)

#agregando un elemento a la lista en un indice especifico
lista.insert(2, 150)

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista por su indice
lista.pop(0) #-1 para eliminar el ultimo.

#removiendo un elemento de la lista por su valor
lista.remove(100)

#eliminando todo los elementos
#lista.clear()

#ordenar la lista
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(150)



print(elemento_encontrado)