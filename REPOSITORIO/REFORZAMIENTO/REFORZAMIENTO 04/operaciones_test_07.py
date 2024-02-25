"""7. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla."""

import random

def generar_numeros():
    numeros = [random.randint(0, 100) for _ in range(30)]
    print("Lista de 30 números enteros aleatorios entre 0 y 100:")
    print(numeros)
    return numeros

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
    return lista_ordenada
