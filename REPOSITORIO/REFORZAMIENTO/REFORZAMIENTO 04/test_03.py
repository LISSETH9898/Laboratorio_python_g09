"""3. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""


def encontrar(diccionario, key):
    try:
        valor = diccionario[key]
        print("El valor de '{}' es: {}".format(key, valor))
    except KeyError:

        print("Error: La clave '{}' no está presente en el diccionario.".format(key))
        print("Por favor, ingrese una clave válida presente en el diccionario.")


persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}

encontrar(persona, "profesion")
