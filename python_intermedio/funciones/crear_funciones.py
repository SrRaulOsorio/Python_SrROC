#creando una funcion simple
def saludar():
    print("Hello my creador como estas?")
    
#ejecutando funcion simple  
saludar()


#funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else :
        adjetivo = "amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")
    
saludar("Raul","hombre")
saludar("Ana","Mujer")
saludar("Frank","")

#funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghijklmnñopqrstuvwxyz"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2 
    c2 = num
    c3 = num - 5 
    contraseña = (f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}")
    return contraseña, num

#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(3)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")
