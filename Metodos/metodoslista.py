#Creando lista con list
lista = list([18,21,1979,False,True])

#devuelve la cantidad de objetos en la lista
cantidad_elementos = len(lista)

#agrego elemento a la lista
lista.append(2001)

#agrega elemento a la lista en un indice especifico
lista.insert(2,34)

#agrega varios elementos a la lista (se agregan [])
lista.extend([False,1.82])

#elimina elemento de la lista por su indice
#-1 para eliminar el ultimo elemento de la lista
lista.pop(0)

#remueve elemento por su valor
lista.remove(21)

#elimina todos los elementos de la lista
#lista.clear()

#ordena los elementos de forma ascendente
#lista.sort(reverse=true) nos invierte la lista
lista.sort()

#la lista que se creo en un principio la invierte
lista.reverse()
print(lista) 