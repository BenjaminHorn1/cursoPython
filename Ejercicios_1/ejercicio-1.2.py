#le pedimos al usuario que nos diga una frase
frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlas')
print(f'Dalto lo diria en {cantidad_de_palabras/2/1.3} segundos')

#en caso de que tarde mas de un minuto en decirlas le decimos que pare
if cantidad_de_palabras > 120:
    print("No te pedi que me cuentes la vida")