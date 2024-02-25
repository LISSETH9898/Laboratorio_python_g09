"""8. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python."""


import math

def cargar_entero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

def mostrar_raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    print("La raíz cuadrada de {} es: {}".format(numero, raiz_cuadrada))

def mostrar_cuadrado_cubo(numero):
    cuadrado = numero ** 2
    cubo = numero ** 3
    print("El cuadrado de {} es: {}".format(numero, cuadrado))
    print("El cubo de {} es: {}".format(numero, cubo))
