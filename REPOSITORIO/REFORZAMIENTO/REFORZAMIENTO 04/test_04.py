"""4. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)"""

def encontrar(a, b):
    try:
        resultado = a / b
        print("El resultado de la división es: {}".format(resultado))
    except TypeError:
        print("Error: No se puede realizar la operación con los tipos de datos proporcionados.")
        print("Por favor, asegúrate de que los operandos sean numéricos.")

a = "Hello Pythonista"

encontrar(a, 0)
