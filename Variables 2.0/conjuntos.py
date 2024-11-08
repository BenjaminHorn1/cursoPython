#creando un conjunto con set
conjunto = set(["dato1" , "dato2" ,])

#metiendo un conjunto dentro de otro conjunto con frozenset
conjunto1 = frozenset(["dato1" , "dato2"])
conjunto2 = {conjunto1 , "dato3"}

print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verificar si hay algun numero en comun (cuando hay solo un elemento en comun devuelve false)
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)