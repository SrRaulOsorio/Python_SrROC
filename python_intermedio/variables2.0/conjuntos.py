#creando un conjunto con set
conjunto = set(["dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#teorioa de conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#verificar si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificar si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

#verificar si hay algun elemento en comun
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)