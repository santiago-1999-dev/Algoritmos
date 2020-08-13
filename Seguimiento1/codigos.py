import fibonacci
import time

n= int(input("Ingrese la posicion a conocer dentro de fibonacci: \n"))
inicio = time.time()
fibonacci.caso1(n) 
final = time.time()
tiempo_caso1 = final-inicio
print(tiempo_caso1)

inicio = time.time()
fibonacci.caso2(n)
final = time.time()
tiempo_caso2 = final-inicio
print(tiempo_caso2)

if tiempo_caso1>tiempo_caso2:
    print("Es mejor el caso 2")
else: 
    print("Es mejor el caso 1")