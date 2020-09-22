#Dada una lista de números enteros devuelva otra con los números divisibles por 7
lista = [12,14,7,21,49,23,45,46,574,32,54]
divSiete = lambda valor : valor % 7 == 0
listaDivisibles = list (filter (divSiete, lista))
print (listaDivisibles)

#Dada una lista de nombres de estudiante devuelva otra con los nombres de un largo menor a 5.
nombres = ['Mafer', 'Daniel', 'Ana','Sara', 'Jorge', 'Yamith', 'Ema','Jair']
nombresCortos = lambda elemento : len (elemento) < 5
listaNombresFiltrados = list (filter (nombresCortos, nombres))
print (listaNombresFiltrados)

#Dada una lista de números devuelva los pares
lista = [12,14,7,21,49,23,45,46,574,32,54]
pares = lambda elemento : elemento % 2 == 0
listaPares = list (filter(pares, lista))
print (listaPares)

# Dada una lista de números devuelva los impares
lista = [12,14,7,21,49,23,45,46,574,32,54]
impares = lambda elemento : elemento % 2 != 0
listaImpares = list (filter(impares, lista))
print (listaImpares)

#Dada una lista de nombres devuelva únicamente aquellos que inician con la letra E
nombres = ['Mafer', 'Daniel', 'Ana','Sara', 'Jorge', 'Yamith', 'Ema','Jair','Elena','Emanuel']
nombresE = lambda elemento : elemento[0] ==  'E'
listaNombresFiltrados = list (filter (nombresE, nombres))
print (listaNombresFiltrados)

#Dada una lista de edades solo devuelva los mayores de edad
listaEdades = [12,14,7,21,49,23,45,46,74,32,54]
mayores = lambda elemento : elemento >= 18
listaMayores = list (filter(mayores, listaEdades))
print (listaMayores)

#Dada una lista frases devuelva únicamente aquellas frases que no tengan la palabra “odian”
frases = ['Todos debemos ser positivos',
          'Aquellos que odian la derrota estan destinados a no crecer',
          'Hay hombres que hacen sentir pequeños a otros pero los hombres realmente grandes hacen sentir gigantes a los que lo rodean',
          'Sobre todo lo que quieres cambiar cambia tu mente pues es el único terreno que te pertenece cabalmente',
          'Aquellos que odian a su projimo acarrearan mala salud a su vida',
          'la gente muere cuando es olvidada',
          'Te acuerdas de tu tataraabuelo? crees que tu tataranieto se acuerde de ti?']
noAlOdio = lambda elemento : 'odian' not in elemento
frasesFiltradas = list (filter(noAlOdio, frases))
print (frasesFiltradas)