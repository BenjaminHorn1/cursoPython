#primero anotar los datos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min 
diferencia_con_min = round(99.4,1)
diferencia_con_max = 100 - dalto_curso  / otros_cursos_max 
diferencia_con_max = round(99.78571,1)
diferencia_con_prom = 100 - dalto_curso / otros_cursos_prom 
diferencia_con_prom = round(99.625,1)

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando diferencias de ejercicio A
print("------------------------------------------------------------------------------------")
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_prom}% menos que el promedio')
print("------------------------------------------------------------------------------------")

#mostrando diferencia de ejercicio B
print(f'Un curso promedio elimino un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino un {tiempo_vacio_dalto}% de tiempo vacio')
print("------------------------------------------------------------------------------------")

#mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos promedios equivale a ver {dalto_curso * 100 // otros_cursos_prom / 10} de este curso')
print("------------------------------------------------------------------------------------")