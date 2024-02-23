"""
1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.

"""

def numero_aleatorio():
    numeros = []
    for i in range(10):
        num = int(input("Ingrese el número {}: ".format(i+1)))
        numeros.append(num)
    return numeros

def numeros_no_repetidos(lista):
    numeros_no_rep = list(set(lista))
    print("Números no repetidos: {}".format(numeros_no_rep))
    return numeros_no_rep

def ordenar_numeros(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    print("Lista ordenada de menor a mayor: {}".format(ascendente))
    print("Lista ordenada de mayor a menor: {}".format(descendente))
    return ascendente, descendente

def mayor_numero_par(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    mayor_par = max(numeros_pares)
    print("Mayor número par de la lista: {}".format(mayor_par))
    return mayor_par

numeros_aleatorios = numero_aleatorio()
numeros_no_rep = numeros_no_repetidos(numeros_aleatorios)
ascendente, descendente = ordenar_numeros(numeros_no_rep)
mayor_par = mayor_numero_par(numeros_no_rep)
