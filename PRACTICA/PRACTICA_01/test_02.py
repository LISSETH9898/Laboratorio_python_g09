"""Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""

import random

lista_original = [ ]

for _ in range(11):
    lista_original.append(random.randint(1,20))

print("Mi lista aleatoria es: {}".format(lista_original))


lista_cubos = [num ** 3 for num in lista_original]
print("El cubo de la lista: {} es: {}".format(lista_original,lista_cubos))

lista_cuadrados = [n ** 2 for n in lista_original]
print("El cuadrado  de la lista: {} es: {}".format(lista_original,lista_cuadrados))

suma = sum(lista_cubos)+sum(lista_cuadrados)
print("La suma de {} y {} es: {}".format(lista_cubos,lista_cuadrados,suma))