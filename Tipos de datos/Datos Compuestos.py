lista = ["Benjamin","Horn",1.83] #Se pueden modificar
tupla = ("Benjamin","Horn",1.83,"Horn") #No se pueden modificar
print(tupla[2])

conjunto = {"Benjamin","Horn",1.83,"Horn"} #No puedo acceder al indice pero si reconstruir
print(tupla)

diccionario = {
    'nombre' : "Benjamin",
    'apellido' : "Horn",
    'es_bueno' : True,
    'altura' : 1.83,
    'dato_duplicado' : "Horn"
}
print(diccionario["es_bueno"])
print(diccionario["apellido"])
print(diccionario["dato_duplicado"])
print(diccionario["altura"])