#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "ruben aguirre"
numeros = [0,1,2,3,4,5,6,7,8,9]
#evitando que se coama una fruta que no le guste (continue)
for fruta in frutas:
    if fruta == "durazno":
        continue
    print(f"Me voy a comer una: {fruta}")
    
    
#evitando se siga ejecutando cuando llege hasta donde queremos (break)
for fruta in frutas:
    if fruta == "granada":
        print(f"explotas por que la {fruta} es una bomba")
        break
   
   
#recorriendo una cadena
for letra in cadena:
    print(letra)
    
    
#creando lista de numeros duplicados
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*5)
    
print(numeros_duplicados)
    
    
#lista con una sola linea de codigo
numeros_duplicados =[x*5 for x in numeros]
print(numeros_duplicados)