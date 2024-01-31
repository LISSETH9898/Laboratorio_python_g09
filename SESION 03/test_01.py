"""Entrdas y salidas"""


usuario = input("Ingrese su nombre de usuario: ")
nombre = input ("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print("Su cuenta es: {}".format(usuario))
print("Bienvenido/a: {}".format(nombre))

actualizar = int(edad) + 15
print("Su edad actualizada es: {}".format(actualizar))