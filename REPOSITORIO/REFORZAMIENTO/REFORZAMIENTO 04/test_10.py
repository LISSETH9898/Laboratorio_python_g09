"""10. Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas."""


def guardar_usuario_en_agenda():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")


    datos_usuario = f"{nombre},{apellido},{edad}\n"


    with open("agenda.txt", "a") as file:
        file.write(datos_usuario)

    print("Usuario guardado en agenda.txt")


guardar_usuario_en_agenda()
