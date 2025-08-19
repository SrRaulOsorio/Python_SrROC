#recorriendo listas con for
animales = ["perro","gato","loro","cocodri","pez","serpirnete","ave","mono","pantera","leon"]
numeros = [0,1,2,3,4,5,6,7,8,9]

#recorriendo lista animales
for animal in animales:
    print(f"ahora la variable es: {animal}")
    
#recorriendo lista numeros
for numero in numeros:
    resultado = numero 
    print(resultado)
    
#interando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#no optima
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    #print(type[num])
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
    
#usando el for else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print(f"el bucle ha terminado.")