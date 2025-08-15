#promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#promedio de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_promedio = 100 - dalto_curso / crudo_dalto * 100

#calculando el promedio de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio /10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto /10

print("------------------")
print("El curso de Dalto dura:")
#mostrar los resultados
print(f" - un {diferencias_con_min}% menos que el mas rapido")
print(f" - un {diferencias_con_max}% menos que el mas lento")
print(f" - un {diferencias_con_promedio}% menos que el promedio")
print("------------------")

#mostrando la cantidad de espacios vaciosque se remueven (ejercicio B)
print(f"un curso promedio elimina un: {tiempo_vacio_promedio}% de tiempo vacio")
print(f"este curso elimino un: {tiempo_vacio_dalto}% de tiempo vacio")
print("------------------")

#mostrando diferencia si los cursoso duraran 10h
print(f"ver 10h de este curso equivale a ver: {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otrsos cursos")
print(f"ver 10h de otros curso equivale a ver: {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
print("------------------")