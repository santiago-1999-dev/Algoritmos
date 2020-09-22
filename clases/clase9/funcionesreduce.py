#Obtenga la resta de todos los elementos de una lista
from functools import reduce
lista = [12,14,7,21,49,23,45,46,574,32,54]
restador = lambda acumulado = 0, elemento = 0: acumulado - elemento
restados = reduce (restador, lista)
print (restados)

# Dada una lista de palabras devolver una frase
from functools import reduce
palabras = ['Hola', 'como', 'estan','?', 'Espero', 'que ', 'esten', 'aprendiendo','muuchoo!!']
union = lambda acumulado = '', valor = '' : acumulado + ' ' + valor
frase = reduce(union, palabras)
print (frase)

# Dada una lista de números enteros entregue la sumatoria de todos elementos tras haber sido divididos por dos
from functools import reduce
lista = [12,14,7,21,49,23,45,46,574,32,54]
sumador = lambda acumulado = 0, elemento = 0: acumulado + (elemento/2)
sumados = reduce (sumador, lista)
print (sumados)

#Devuelva el promedio de una lista de números
from functools import reduce
lista = [12,14,7,21,49,23,45,46,574,32,54]
sumador = lambda acumulado = 0, elemento = 0: acumulado + elemento
promedio = reduce (sumador, lista)/len (lista)
print (promedio)

# Que multiplique todos los elementos de la lista entre si
from functools import reduce
lista = [12,14,7,21,49,23,45,46,574,32,54]
multiplicador = lambda acumulado = 0, elemento = 1: acumulado * elemento
multiplicado = reduce (multiplicador, lista)/len (lista)
print (multiplicado)