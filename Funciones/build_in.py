numeros = [4,7,12,87,134]

#encontrando el numero mayor en una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor en una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.4356,2)
print(numero)

#retorna false -> 0, false, ninguno, vacio / true -> num distinto de 0, true, cadena, datos no vacios
resultado_bool = bool(0)
print(resultado_bool)

#retorna true si todos los datos son verdaderos
resultado_all = all([34,"Boca",[45,23,12]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)