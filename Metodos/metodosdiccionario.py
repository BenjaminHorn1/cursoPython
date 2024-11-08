diccionario = {
    "nombre" : "Benjamin",
    "apellido" : "Horn",
    "altura" : 180
}
#keys devuelve las claves (tambien sirve para iterar)
claves = diccionario.keys()

#get nos devuelve el valor de la clave (no hay excepcion, si no encuntra devuelve none y el programa continua)
valor_clave = diccionario.get("nombre")

#elimina todo el diccionario 
#diccionario.clear()

#Eliminando un elemento del diccionario 
diccionario.pop("apellido")

#obteniendo un elemto dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)