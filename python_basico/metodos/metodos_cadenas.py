cadena1 = "soy, pro, master, poderoso, grandioso"
cadena2 = "pro"

#convierte a mayuscula
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#convierte a primera letra mayuscula
primera_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena
busqueda_find = cadena1.find("o")

#Buscamos una cadena en otra cadena con index
busqueda_index = cadena1.index("o")

#si es numerico, devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devuelve true, sino devuelve false
es_alfanumerico = cadena1.isalpha()

#buscamos en una cadena y devuelve las coincidencias
contar_coincidencias = cadena1.count("h")

#contamos cuantos caracteres hay en una cadena
contar_caracteres = len(cadena1)

#Verificar si la cadena inicia con un caracter especifico
empieza_con = cadena1.startswith("h")

#Verificar si la cadena termina con un caracter especifico
termina_con = cadena1.endswith("y")

#reemplaza un pedazo de la cadena dada, por otra
cadena_nueva = cadena1.replace("soy", "SOYYYYYY")

#separar cadena por la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)