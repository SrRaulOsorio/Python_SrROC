#creando funciones que suma numeros
def sumar_dos():
    #iniciando un buble
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanza una excepcion pedirle que reingres datos 
        except ValueError as e:
            print("Te pedi un numero, no te hagas el gracioso")
            print(f"ERROR: {e}")
        #asi todo salio bien termina el bucle
        else:
            break
        finally:
            print("Manejo de excepciones dinalizado")
            
    #mostrando el resultado
    return resultado

print(sumar_dos())