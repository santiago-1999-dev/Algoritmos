#FuncionesLabda
potenciador = lambda base=0, exponente =0 : base**exponente
print (potenciador(2,4))
#----------------------------------------------------------------------
repetidor = lambda palabra, numero : palabra*numero
print (repetidor("Hola: ", 2))
#----------------------------------------------------------------------
lista_1 = [1,2,3,4]
lista_2 = [7,8,9,6]
Maximo = lambda lista1, lista2 : print(max(lista1), max(lista2))
Maximo (lista_1, lista_2)
#-----------------------------------------------------------------------

#FuncionesMap
listaNotas = [3, 2, 2, 7, 4]
exponente =lambda  elemento: elemento**2
listaCuadrados = list(map(exponente, listaNotas))
print(listaCuadrados)

listaNotas = [3, 2, 2, 7, 4]
Divicion =lambda  elemento: (elemento)/(max(listaNotas))
listaCuadrados = list(map(Divicion, listaNotas))
print(listaCuadrados)

#FunncionesFilter
listaNumeros = [1, 2, 3, 35, 23, 4, 8, 9, 21]
listadivisibles = []

divisibles = lambda elemento : elemento %7 ==0
divisibles = list (filter(divisibles, listaNumeros))
print (divisibles)

#FuncionesReduce
