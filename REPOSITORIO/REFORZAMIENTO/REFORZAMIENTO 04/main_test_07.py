"""7. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla."""

import operaciones_test_07
def datos():
    lista_numeros = operaciones_test_07.generar_numeros()

    lista_ordenada = operaciones_test_07.ordenar_lista(lista_numeros)

if __name__ == "__main__":
    datos()
