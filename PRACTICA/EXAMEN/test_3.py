"""
3. (3 ptos) Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.

"""


import time

def calcular_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print("Tiempo de ejecución de '{}': {} segundos".format(func.__name__, fin - inicio))
        return resultado
    return wrapper

@calcular_tiempo
def multiplicacion(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print("Ejemplo 1:")
print("Resultado de la multiplicación:", multiplicacion(2,3,4))
print()

print("Ejemplo 2:")
print("Resultado de la multiplicación:", multiplicacion(5,6,7,8))
print()

print("Ejemplo 3:")
print("Resultado de la multiplicación:", multiplicacion(9,10,11,12,13))

