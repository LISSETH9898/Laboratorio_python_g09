"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""


def encontrar(lista, indice):
    try:
        elemento = lista[indice]
        print("El elemento en el índice {} es: {}".format(indice,elemento))
    except IndexError:
        print("Error: El índice {} está fuera del rango de la lista." .format(indice))
        print("Por favor, ingrese un índice válido dentro del rango de la lista.")


lista = [2, 6, 10, 4, 5, 23, 1]

encontrar(lista, 10)
