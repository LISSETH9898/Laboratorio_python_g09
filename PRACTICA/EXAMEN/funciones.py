"""2. (3 ptos) Crear un programa para gestionar un fichero con diferentes
tipos de operaciones numéricas.
Reglas:
- El programa tendrá la función de crear el fichero con el nombre “notas.txt”
crearlo si no existe en la ruta indicada y el cual será dividido en dos
archivos, uno principal donde se llamará a las funciones que realizarán
distintas operaciones en el otro archivo la cual será llamada funciones.py
(aplicar módulos)

- Crear una función donde se pedirá el tamaño de lista será ingresado por
consola (los números serán llenados de manera aleatoria dentro de la lista),
esta lista será escrita dentro del file “notas.txt”
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.

• Cerrar respectivamente los ficheros cada vez que se abra."""


import math
import random

def generar_lista(tamaño):
    return [random.randint(1, 100) for _ in range(tamaño)]

def escribir_lista_en_archivo(lista):
    with open("notas.txt", "a") as archivo:
        archivo.write("Lista de numeros generados:\n")
        for num in lista:
            archivo.write(str(num) + "\n")

def calcular_raices(lista):
    return [math.sqrt(num) for num in lista]

def escribir_raices_en_archivo(raices):
    with open("notas.txt", "a") as archivo:
        archivo.write("\n Raices cuadradas de la lista:\n")
        for raiz in raices:
            archivo.write(str(raiz) + "\n")
