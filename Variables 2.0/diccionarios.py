#creando diccionarios con dict()
diccionario = dict(nombre="Benjamin", apellido="Horn")

#las listas no pueden ser claves usamos frozenset para meter conjuntos
diccionario = {frozenset(["Benjamin","GOAT"]) : "the new"}

#creando diccionario con fromkeys()   Sin valores definidos, devuelve none
diccionario = dict.fromkeys(["nombre","apellido","altura"])

#creando diccionario con fromkeys()   le damos un valor
diccionario = dict.fromkeys(["nombre","apellido","altura"], "Ni idea mostro")

print(diccionario)