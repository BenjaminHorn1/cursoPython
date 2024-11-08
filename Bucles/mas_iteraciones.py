frutas = ["manzana", "banana", "ciruela", "uva" , "durazno", "pera", "naranja"]
cadena = "Dale Boca"
numeros = [2,4,8,12]

#evitando que se coma una ciruela con la sentencia continue
for fruta in frutas:
    if fruta == 'ciruela':
        continue
    print(f"Me voy a comer una: {fruta}")
    
#evitando que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == 'uva':
        break
else:    
     print("terminado")    
    
       
#recorrer una cadena de texto  
for letra in cadena:
    print(letra)   
    
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)      