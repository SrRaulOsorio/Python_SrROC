
#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([5,3,9,10,20,3])

#utilizando el operador* como parametro (args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("lucas",5,3,9,10,20,3 )

print(resultado)