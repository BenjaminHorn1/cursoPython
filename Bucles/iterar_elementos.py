
animales =  ["perro","gato","vaca","pajaro"]
numeros = [10,23,45,67]

#recorriendo lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
    
#recorriendo lista numeros y * 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)    
    
#iterando dos listas del mismo tamano al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')    
    print(f'recorriendo lista 2: {animal}')    
    

#forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])    
    
    
#forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    

#usando el else 
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
    
#todo lo anterior funciona tambien en tuplas y conjuntos             