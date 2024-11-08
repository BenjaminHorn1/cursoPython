cadena1 = "Hola,soy,Benjamin"
cadena2 = "AguanteBocaaaa"
#CONVIERTEN VALOR
#upper nos devuelve texto en mayussculas
#lower devuelve el texto en minusculas
#capitalize devuelve primera mayuscula

#ENCUENTRAN VALOR
#find nos busca la posicion de un objeto, de lo contrario -1
#index si no encuentra tira una excepcion

#NOS REVELAN SI SON NUMERICOS O ALFANUMERICOS
#isnumeric devuelve true si es numerico
#isalpha devuelve true si es alfanumerico     (no usar caracteres especiales)

#CANTIDAD DE COINCIDENCIAS EN LA CADENA
#count nos devuelve la cantidad de coincidencia de una valor
#len contamos cuantos caracteres tiene una cadena (no es un metodo, es una funcion!!!!)

#VERIFICAR 
#startswith nos devuelve true si empieza con el valor asignado
#endswith nos devuelve true si termina con el valor asignado

#REMPLAZAR
#replace cambia una parte de la cadena por otra que se le asigne
#split separa por el parametro dado
resultado = cadena1.split(",")
print(resultado)