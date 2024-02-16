"""3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""


def ingresar_datos():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese números válidos.")

def division():
    while True:
        try:
            num1, num2 = ingresar_datos()
            resultado = num1 / num2
            print("El resultado de la división es:".format(resultado))
            break
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

def suma_incorrecta():
    while True:
        try:
            num1, num2 = ingresar_datos()
            resultado = num1 + num2
            print("La suma de los números es:".format(resultado))
            break
        except ValueError:
            print("Error: Ingrese números válidos.")

def ingresar_lista():
    while True:
        try:
            n = int(input("Ingrese la cantidad de elementos de la lista: "))
            lista = []
            for i in range(n):
                elemento = input("Ingrese el elemento {}: ".format(i+1))
                lista.append(elemento)
            indice = int(input("Ingrese el índice que desea consultar: "))
            print("El elemento en el índice {} es: {}".format(indice, lista[indice]))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para el índice.")
        except IndexError:
            print("Error: El índice está fuera de rango.")


print("División:")
division()

print("\nSuma incorrecta:")
suma_incorrecta()

print("\nÍndice de lista:")
ingresar_lista()
