#def frase(nombre,apellido,adjetivo):
#    return f"hola {nombre} {apellido}, sos muy {adjetivo}"
#
#frase_resultante = frase("Raul","Osorio","Capo")
#print(frase_resultante)

#creando la misma funcion pero con parametros opcional o parametro por defecto.
def frase(nombre,apellido,adjetivo = "Listo"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Raul","Osorio","inteligente")
print(frase_resultante)