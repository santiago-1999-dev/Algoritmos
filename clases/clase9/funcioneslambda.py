#Que devuelva el exponte n de un número dado
potenciador = lambda base, exponente : base ** exponente
print (potenciador (2,4))

#Muestre en pantalla n veces un string ingresado
mostrarPalabra = lambda palabra, cantidad_veces : print (palabra*cantidad_veces)
mostrarPalabra ('Me gusta programar en python \n', 15)

#Muestre en pantalla el máximo número de dos listas ingresadas
encontrarMaximos = lambda lista1, lista2 : print (max(lista1), max (lista2))
edadesGrupoA = [18,29,23,26,27,20,22,19,16]
edadesGrupoB = [18,49,43,26,27,40,22,19,16]

encontrarMaximos (edadesGrupoA,edadesGrupoB)

#Devuelva verdadero o falso dependiendo si un número es par o no
par = lambda valor : valor %2 == 0
print (par(2))
print (par(3))

#Devuelva verdadero o falso dependiendo si un número es impar o no
impar = lambda valor : valor % 2 != 0
print (impar (2))
print (impar (3))

#Que devuelva la unión de dos palabras
unionPalabras = lambda palabra1 , palabra2 : palabra1 + ' ' + palabra2
print (unionPalabras('Hola','amigo')) 

#Que dado un nombre salude a la persona ingresada
preguntaNombre = 'Ingrese su nombre por favor : '
nombre = input(preguntaNombre)
saludar = lambda name = '' : print (f'Bienvenido {name} a este programa')
saludar(nombre)

#Que dada una palabra devuelva el largo de la misma
palabraDada = 'Hola'
lenPalabra  = lambda palabra : len (palabra)
print (lenPalabra(palabraDada))

#Que utilizando la anterior muestre en pantalla el resultado
showLen = lambda funcion, palabra : print (funcion(palabra))
showLen(lenPalabra, palabraDada)

#Devuelva el área de un triángulo dada su base y altura
areaTriangulo = lambda base, altura : base*altura/2
area = areaTriangulo (8,4)
print (area)

#Calcule el imc sabiendo la altura y el peso (imc = peso / altura^2)
imcCalculator = lambda peso, altura : peso/(altura**2)
imc= imcCalculator(80,1.67)
print (imc)




#