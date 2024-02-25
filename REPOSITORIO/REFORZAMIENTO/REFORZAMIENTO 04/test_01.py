"""Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""


def encontrar (a,b):
    try:
        suma = a + b
    except TypeError:
        print("No se puede sumar, por favor ingresar un numero")
    else:
        print(suma)

encontrar(80 ,"Hola Pythonista")