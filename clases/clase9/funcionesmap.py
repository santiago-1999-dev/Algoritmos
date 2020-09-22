#Devuelva el cuadrado de cada elemento de la lista
potenciador = lambda valor : valor ** 2
lista = [2,5,6,12,25,43,21]
listaCuadrados = list (map(potenciador, lista))
print (listaCuadrados)

#Divida a todos los elementos de la lista por el mayor número de la misma
lista = [2,5,6,12,25,43,21]
maximo = max (lista)
normalizador = lambda valor : valor / maximo
listaNormalizada = list (map(normalizador, lista))
print (listaNormalizada)

#Le reste un número n a la lista
lista = [2,5,6,12,25,43,21]
valor_n = 2
restador = lambda elemento : elemento  - valor_n

listaRestada = list (map(restador, lista))
print (listaRestada)

#Le sume un número n a la lista
lista = [2,5,6,12,25,43,21]
valor_n = 2
sumador = lambda elemento : elemento  + valor_n

listaSumada = list (map(sumador, lista))
print (listaSumada)

#Todos los elementos multiplicados * 5
lista = [2,5,6,12,25,43,21]
multiplo = 5
multiplicador = lambda elemento : elemento * multiplo

listaRestada = list (map(multiplicador, lista))
print (listaRestada)

